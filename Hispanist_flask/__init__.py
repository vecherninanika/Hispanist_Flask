import os
from flask import Flask
from .database import db
from flask_mail import Mail
from flask_login import LoginManager

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

    return app
