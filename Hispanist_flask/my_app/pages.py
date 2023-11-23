from flask import (
    Blueprint,
    render_template,
    request, redirect,
    session,
    flash,
    get_flashed_messages,
    url_for,
    abort,
)
from .models import *
from flask_mail import Message
from flask_login import current_user, login_required
from sqlalchemy.exc import SQLAlchemyError
from Hispanist_flask import mail
from Hispanist_flask.my_app.main_page import log_error


module = Blueprint('pages', __name__, template_folder='Hispanist_Flask/templates/pages', static_folder='static/pages', url_prefix='/')


@module.route('/rating')
def rating():
    """Page that shows rating of Spanish schools and universities."""
    schools = School.query.all()
    universities = University.query.all()
    return render_template("my_app/pages/rating.html", schools=schools, universities=universities)


@module.route('/books')
def books():
    books = Book.query.all()
    return render_template('my_app/pages/books.html', books=books)


@module.route('/videos')
def videos():
    """Page that shows rating of Spanish schools and universities."""
    channels = Video.query.filter(Video.type=='канал').all()
    videos = Video.query.filter(Video.type=='видео').all()
    return render_template("my_app/pages/videos.html", channels=channels, videos=videos)


@module.route('/article/<id>', methods=['GET', 'POST'])
def article(id):
    """
    article: instance of article that the method gets from the form in html to render one article.
    Page that renders one article.
    """
    article_object = Article.query.filter(Article.id == id).one()
    return render_template('my_app/pages/article.html', article=article_object)


@module.route('/learn_words', methods=['GET', 'POST'])
@login_required
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
        except SQLAlchemyError as e:
            log_error('Error while querying database', exc_info=e)
            flash('Добавление слова не удалось', 'danger')
            abort(500)
        session.modified = True
    return render_template('my_app/pages/learn_words.html', words=words)


@module.route('/olimpiads')
def olimpiads():
    return render_template('my_app/pages/olimpiads.html')


@module.route('/lessons', methods=["GET", "POST"])
def lessons():
    if request.method == 'POST':
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        msg = Message('Клиент оставил обращение на сайте', recipients=[email])
        msg.body = f'Номер телефона клиента: {phone}, сообщение от клиента: {message}'
        mail.send(msg)
        flash('менеджер свяжется с вами в течение суток')
        return redirect(url_for('pages.lessons'))
    return render_template('my_app/pages/lessons.html')
