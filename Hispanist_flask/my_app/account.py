from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    session,
    flash,
    url_for,
    abort
)
from .models import *
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, login_required
from sqlalchemy.exc import SQLAlchemyError
from Hispanist_flask import login_manager
from Hispanist_flask.my_app.main_page import log_error


module = Blueprint('account', __name__, template_folder='./templates/account', static_folder='./static/account', url_prefix='/')


@module.route('/signin', methods=['POST', 'GET'])
def signin():
    """Registration and authorization."""
    if request.method == 'POST':
        username = request.form.get('username')
        name = request.form.get('name')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        action = request.form.get('action')
        if action == 'signin':
            try:
                user = User.query.filter(User.username == username).one()
            except Exception:
                flash('Пользователь не найден. Зарегистрируйтесь')
                return render_template('my_app/account/signin.html')
            if check_password_hash(user.password, password):
                login_user(user)
                session["Cart"] = []
                return redirect(url_for('main_page.index'))
            else:
                flash('Неправильный пароль')
                return render_template('my_app/account/signin.html')
        else:
            if password != confirm_password:
                flash("Пароли не совпали")
                return render_template('my_app/account/signin.html')
            password = generate_password_hash(password)
            if User.query.filter(User.username==username):
                flash("Это имя пользователя занято")
                return render_template('my_app/account/signin.html')
            new_user = User(name=name, username=username, password=password, role=2)
            try:
                db.session.add(new_user)
                db.session.commit()
            except SQLAlchemyError as e:
                log_error('Error while querying database', exc_info=e)
                flash('Добавление пользователя не удалось')
                abort(500)
            session.modified = True
            print('NEW USER CREATED')
            login_user(new_user)
            session["Cart"] = []
            return redirect(url_for('main_page.index'))
    return render_template('my_app/account/signin.html')


@module.route('/signout')
@login_required
def signout():
    """Signout action."""
    logout_user()
    return redirect(url_for('main_page.index'))


@login_manager.user_loader
def load_user(user_id):
    """Function that gets the current user."""
    return User.query.filter(User.id == user_id).first()


@module.route('/profile')
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
    return render_template('my_app/account/profile.html', user=user, articles=articles)


@module.route('/edit', methods=['POST', 'GET'])
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
                flash('Вы неправильно ввели свой старый пароль')
                return redirect(url_for('account.edit'))
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
        except SQLAlchemyError as e:
            log_error('Error while querying database', exc_info=e)
            flash('Добавление пользователя не удалось', 'danger')
            abort(500)
        return redirect(url_for('account.profile'))
    return render_template('my_app/account/edit.html', user=user)
