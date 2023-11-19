import flask_admin as admin
from flask_admin import helpers, expose
import flask_login as login
from flask import redirect, url_for
from models import User

class MyAdminIndexView(admin.Admin):
    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated:
            return redirect(url_for('login'))
        admin = User.query.filter(User.id==login.current_user.get_id()).first()
        if admin.role == 1:
            return super(MyAdminIndexView, self).index()
        return redirect(url_for('login'))
