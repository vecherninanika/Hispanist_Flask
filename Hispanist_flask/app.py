from flask import Flask, render_template, url_for, request, redirect, make_response, session, flash, get_flashed_messages
from models import *
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
from os import getenv
from dotenv import load_dotenv
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from api_bp.api import api_bp
from  sqlalchemy.sql.expression import func


app = Flask(__name__)

load_dotenv()
DISCONNECT = getenv('DISCONNECT')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://app:hispanist123@localhost:5436/hispanist_db'
app.secret_key = getenv('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = getenv('MAIL')
app.config['MAIL_PASSWORD'] = getenv('PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = getenv('MAIL')
app.config['FLASK_ADMIN_SWATCH'] = 'simplex'

mail = Mail(app)
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
app.register_blueprint(api_bp, url_prefix='/api')

admin = Admin(app, name='microblog', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(School, db.session))
admin.add_view(ModelView(University, db.session))
admin.add_view(ModelView(Article, db.session))


@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    """Function that renders the homepage."""
    cart = session['Cart'] if 'Cart' in list(session.keys()) else []
    correct = ''
    topics = Topic.query.all()
    articles = Article.query.all()
    question = Question.query.order_by(func.random()).first()
    options = question.options.split(',')
    if request.method == 'POST':
        # Answer a question from Espana ayer y hoy
        answer = request.form.get('answer_for_eayh_question')
        print('ANSWER', answer)
        if answer:
            # question = Question.query.filter(answer in question.answers)
            if answer == question.answer:
                correct = 'Правильно! +1 балл'
                print('CORRECT', correct)
                user = User.query.filter(User.username == current_user.username).first()
                print('USER', user)
                if not user:
                    flash('Зарегистрируйтесь, чтобы получить баллы за этот вопрос')
                    print('Зарегистрируйтесь, чтобы получить баллы за этот вопрос')
                else:
                    user.points += 1
                    db.session.commit()
            else:
                correct = 'Неправильно'
        # Filter articles by topic
        topic_name = request.form.get('topic')
        print('TOPIC', topic_name)
        articles = Article.query.filter(Article.topics.any(Topic.name==topic_name)).all()
        if topic_name == 'Все темы':
            articles = Article.query.all()
        print(articles)

    return render_template("index.html", articles=articles, cart=cart, topics=topics, question=question, correct=correct, options=options)


# LOGIN


@app.route('/signin', methods=['POST', 'GET'])
def signin():
    """Registration and authorization."""
    if request.method == 'POST':
        session["Cart"] = []
        username = request.form.get('username')
        name = request.form.get('name')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        action = request.form.get('action')
        if action == 'signin':
            try:
                user = User.query.filter(User.username == username).one()
            except Exception:
                print(('Пользователь не найден. Зарегистрируйтесь'))
                flash('Пользователь не найден. Зарегистрируйтесь')  # TODO
                return render_template('signin.html')
            if check_password_hash(user.password, password):
                print('SIGN IN SUCCESSFULL')
                login_user(user)
                # flash(f'Вы вошли в аккаунт {username}!')
                return redirect(url_for('index'))
        else:
            if password != confirm_password:
                flash("Пароли не совпали")
                print("Пароли не совпали")
                # return render_template('signin.html')
            password = generate_password_hash(password)
            if User.query.filter(User.username==username):
                flash("Это имя пользователя занято")
                print("Это имя пользователя занято")
                return render_template('signin.html')
            new_user = User(name=name, username=username, password=password, role=2)
            try:
                db.session.add(new_user)
                db.session.commit()
            except Exception:
                flash("Добавление пользователя не удалось")
            session.modified = True
            print('NEW USER CREATED')
            login_user(new_user)
            flash('Вы зарегистрированы!')
            return redirect(url_for('index'))
    return render_template('signin.html')


@app.route('/signout')
@login_required
def signout():
    """Signout action."""
    logout_user()
    return redirect(url_for('index'))


@login_manager.user_loader
def load_user(user_id):
    """Function that gets the current user."""
    return User.query.filter(User.id == user_id).first()


@app.route('/profile')
@login_required
def profile():
    """Profile."""
    user = User.query.filter(User.username == current_user.username).one()
    articles = []
    if 'Cart' in session:
        for article_id in session['Cart']:
            article = Article.query.filter(Article.id == article_id).first()
            articles.append(article)
        session.modified = True
    return render_template('profile.html', user=user, articles=articles)


@app.route('/edit', methods=['POST', 'GET'])
@login_required
def edit():
    """Page where you can edit your profile information."""
    user = User.query.filter(User.username == current_user.username).one()
    if request.method == 'POST':
        username = request.form.get('username')
        name = request.form.get('name')
        old_password = request.form.get('old_password')
        password = request.form.get('password')
        level = request.form.get('level')
        region = request.form.get('region')
        gender = request.form.get('gender')
        age = request.form.get('age')
        goal = request.form.get('goal')
        info = request.form.get('info')
        if username:
            user.username = username
        if name:
            user.name = name
        if old_password:
            if check_password_hash(user.password, old_password):
                user.password = generate_password_hash(password)
            else:
                print('Вы неправильно ввели свой старый пароль')
                flash('Вы неправильно ввели свой старый пароль')
                return redirect(url_for('edit'))
        if level:
            user.level = level
        if region:
            user.region = region
        if gender:
            user.gender = gender
        if age:
            user.age = age
        if goal:
            user.goal = goal
        if info:
            user.info = info
        try:
            db.session.commit()
        except Exception:
            flash("Добавление пользователя не удалось")
            return redirect(url_for('edit'))
        return redirect(url_for('profile'))
    return render_template('edit.html', user=user)


# PAGES


@app.route('/rating')
def rating():
    """Page that shows rating of Spanish schools and universities."""
    schools = School.query.all()
    universities = University.query.all()
    return render_template("rating.html", schools=schools, universities=universities)


@app.route('/books')
def books():
    books = Book.query.all()
    return render_template('books.html', books=books)


@app.route('/videos')
def videos():
    """Page that shows rating of Spanish schools and universities."""
    channels = Video.query.filter(Video.type=='канал').all()
    videos = Video.query.filter(Video.type=='видео').all()
    return render_template("videos.html", channels=channels, videos=videos)


@app.route('/article/<id>', methods=['GET', 'POST'])
def article(id):
    """
    article: instance of article that the method gets from the form in html to render one article.
    Page that renders one article.
    """
    article_object = Article.query.filter(Article.id == id).one()
    return render_template('article.html', article=article_object)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        msg = Message('Клиент оставил обращение на сайте', recipients=[email])
        msg.body = f'Номер телефона клиента: {phone}, сообщение от клиента: {message}'
        mail.send(msg)
        # создать такой template, либо flash-message
        flash('менеджер свяжется с вами в течение суток')
        return redirect(url_for('index'))
    return render_template('contact.html')


@app.route('/learn_words', methods=['GET', 'POST'])
def learn_words():
    words = Word.query.filter(Word.users.any(User.username == current_user.username)).all()
    if request.method == 'POST':
        word = request.form.get('word')
        translation = request.form.get('translation')
        print(word)
        print(translation)
        print(request.form)
        word_obj = Word.query.filter(Word.word==word).all()
        if not word_obj:
            word_obj = Word(word=word, translation=translation)
            db.session.add(word_obj)
        user = User.query.filter(User.username == current_user.username).one()
        word_obj.users.append(user)
        print(word_obj)
        try:
            db.session.commit()
        except Exception:
            flash("Добавление слова не удалось")
            print("Добавление слова не удалось")
        session.modified = True
    return render_template('learn_words.html', words=words)


@app.route('/olimpiads')
def olimpiads():
    return render_template('olimpiads.html')


@app.route('/lessons', methods=["GET", "POST"])
def lessons():
    if request.method == 'POST':
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        msg = Message('Клиент оставил обращение на сайте', recipients=[email])
        msg.body = f'Номер телефона клиента: {phone}, сообщение от клиента: {message}'
        mail.send(msg)
        # создать такой template, либо flash-message
        flash('менеджер свяжется с вами в течение суток')
        return redirect(url_for('lessons'))
    return render_template('lessons.html')

# CART


@app.route('/add_to_cart/<article_id>', methods=['GET', 'POST'])
def add_to_cart(article_id):
    if request.method == 'POST':
        print(213)
        if 'Cart' in session:
            print(214)
            if not int(article_id) in session['Cart']:
                session['Cart'].append(int(article_id))
                session.modified = True
                print(218)
        return redirect(request.referrer)


@app.route('/remove_from_cart/<article_id>', methods=['GET', 'POST'])
def remove_from_cart(article_id):
    if request.method == 'POST':
        item = session['Cart'].remove(int(article_id))
        session.modified = True
    return redirect(request.referrer)


if __name__ == '__main__':
    app.run(debug=True)
