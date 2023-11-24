import flask_admin
import flask_login
from flask import redirect, url_for, flash
from .models import *
from flask_admin import expose
from flask_admin.contrib.sqla import ModelView


class MyAdminIndexView(flask_admin.AdminIndexView):
    """
    Overriding admin index view.
    """

    @expose('/')    # to create views, but in classes
    def index(self):
        """
        Authorization for '/admin' panel.
        Returns: redirect to '/signin' if the user is not logged in or if he is not an admin
        """
        if not flask_login.current_user.is_authenticated:
            flash('Войдите в аккаунт, чтобы зайти в панель админа')
            return redirect(url_for('account.signin'))
        admin = User.query.filter(User.id==flask_login.current_user.get_id()).one()
        if admin.role == 1:
            return super(MyAdminIndexView, self).index()
        flash('У вашего аккаунта нет доступа к панели админа')
        return redirect(url_for('account.signin'))


class MyModelView(ModelView):
    """
    Overriding base ModelView to add authentication for other admin parts.
    """
    column_hide_backrefs = False

    def is_accessible(self):
        """
        This method is used to check if current user is authenticated and his role is Admin.
        """
        if not flask_login.current_user.is_authenticated:
            return False
        admin = User.query.filter(User.id==flask_login.current_user.get_id()).one()
        if admin.role == 1:
            return True
        return False
    

class UserView(MyModelView):
    """
    View for '/admin/user'.
    """
    column_list = ('id', 'name', 'username', 'role', 'level', 'region', 'gender', 'age', 'goal', 'info', 'points', 'words')
    column_searchable_list = ['name']
    column_sortable_list = ['name']


class ArticleView(MyModelView):
    """
    View for '/admin/article'.
    """
    column_list = ('id', 'title', 'text', 'image', 'topics')
    column_searchable_list = ['title']
    column_sortable_list = ['title']


class TopicView(MyModelView):
    """
    View for '/admin/topic'.
    """
    column_list = ('id', 'name', 'articles')
    column_searchable_list = ['name']
    column_sortable_list = ['name']
