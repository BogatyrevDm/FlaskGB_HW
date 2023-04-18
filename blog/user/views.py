from flask import Blueprint, render_template, redirect
from flask_login import login_required
from werkzeug.exceptions import NotFound

from blog.app import login_manager

user = Blueprint("user", __name__, url_prefix='/users', static_folder='../static')


@user.route('/')
def user_list():
    from blog.models import User
    users = User.query.all()
    return render_template('users/list.html', users=users)


@user.route('/<int:pk>')
@login_required
def profile(pk: int):
    from blog.models import User
    # user_name = USERS[pk]
    try:
        user = User.query.filter_by(id=pk).one_or_none()
    except KeyError:
        # raise NotFound(f'User id {pk} not found!')
        return redirect('/users/')
    return render_template('users/profile.html', user=user)
