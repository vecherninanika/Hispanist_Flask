import os
from flask import Flask
from .database import db
from flask_mail import Mail
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

mail = Mail()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    mail.init_app(app)
    login_manager.init_app(app)

    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    from Hispanist_flask.my_app import main_page
    from Hispanist_flask.my_app import pages
    from Hispanist_flask.my_app import account
    from Hispanist_flask.my_app import cart
    from Hispanist_flask.api_bp import api

    app.register_blueprint(main_page.module)
    app.register_blueprint(pages.module)
    app.register_blueprint(account.module)
    app.register_blueprint(cart.module)
    app.register_blueprint(api.api_bp)

    from Hispanist_flask.my_app import admin_view 
    from Hispanist_flask.my_app import models

    admin = Admin(app, index_view=admin_view.MyAdminIndexView(), name='HispanistAdmin', template_mode='bootstrap3')
    admin.add_view(admin_view.UserView(models.User, db.session))
    admin.add_view(admin_view.ArticleView(models.Article, db.session))
    admin.add_view(admin_view.TopicView(models.Topic, db.session))
    admin.add_view(ModelView(models.School, db.session))
    admin.add_view(ModelView(models.University, db.session))
    admin.add_view(ModelView(models.Question, db.session))
    admin.add_view(ModelView(models.Book, db.session))
    admin.add_view(ModelView(models.Word, db.session))


    return app
