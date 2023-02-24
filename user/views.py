from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from constants import USERS

user = Blueprint(name='user', import_name=__name__, static_folder='../static', url_prefix='/users')


@user.route('/')
def user_list():
    return render_template('user/users_list.html',
                           users=USERS
                           )


@user.route('/<int:pk>')
def get_user(pk: int):
    try:
        user = USERS[pk]
    except KeyError:
        raise NotFound(f'User {pk} is not found')
    return render_template('user/user_details.html',
                           username=user
                           )
