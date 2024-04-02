from http import HTTPStatus

from flask import (
    Blueprint,
    abort,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from flask_login import current_user
from Hispanist_flask import login_manager
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql.expression import func

from .models import *

module = Blueprint(
    "main_page",
    __name__,
    template_folder="./templates/main_page",
    static_folder="./static/main_page",
    url_prefix="/",
)


def log_error(*args, **kwargs):
    current_app.logger.error(*args, **kwargs)


@module.route("/index", methods=["GET", "POST"])
@module.route("/", methods=["GET", "POST"])
def index():
    """Function that renders the homepage."""
    cart = session["Cart"] if "Cart" in list(session.keys()) else []
    correct = ""
    topics = Topic.query.all()
    articles = Article.query.all()
    question = Question.query.order_by(func.random()).first()
    options = question.options.split(",")
    if request.method == "POST":
        # Answer a question from Espana ayer y hoy
        answer = request.form.get("answer_for_eayh_question")
        print("ANSWER", answer)
        if answer:
            q = Question.query.filter(Question.options.contains(answer)).first()
            if answer == q.answer:
                correct = "Правильно! +1 балл"
                user = User.query.filter(User.username == current_user.username).first()
                if not user:
                    flash("Зарегистрируйтесь, чтобы получить баллы за этот вопрос")
                else:
                    if user.points:
                        user.points += 1
                    else:
                        user.points = 1
                    try:
                        db.session.commit()
                    except SQLAlchemyError as e:
                        log_error("Error while querying database", exc_info=e)
                        flash("Произошла непредвиденная ошибка")
                        abort(500)
            else:
                correct = "Неправильно"
            flash(correct)
        # Filter articles by topic
        topic_name = request.form.get("topic")
        articles = Article.query.filter(
            Article.topics.any(Topic.name == topic_name)
        ).all()
        if not topic_name or topic_name == "Все темы":
            articles = Article.query.all()
    return render_template(
        "my_app/index.html",
        articles=articles,
        cart=cart,
        topics=topics,
        question=question,
        correct=correct,
        options=options,
    )


@login_manager.unauthorized_handler
def unauthorized():
    if request.blueprint == "api":
        abort(HTTPStatus.UNAUTHORIZED)
    return redirect(url_for("request.referrer"))
