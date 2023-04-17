from flask import Blueprint, render_template, redirect
from werkzeug.exceptions import NotFound



user = Blueprint("user", __name__, url_prefix='/users', static_folder='../static')



@user.route('/')
def user_list():
    from blog.models import User
    users = User.query.all()
    return render_template('users/list.html', users=users)


@user.route('/<int:pk>')
def get_user(pk: int):
    # user_name = USERS[pk]
    try:
        user_name = USERS[pk]
    except KeyError:
        # raise NotFound(f'User id {pk} not found!')
        return redirect('/users/')
    return render_template('users/details.html', user_name=user_name)
