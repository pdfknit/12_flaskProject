from flask import Blueprint, render_template
from flask_login import login_manager
from werkzeug.exceptions import NotFound
from models import User

user = Blueprint(name='user', import_name=__name__, static_folder='../static', url_prefix='/users')


@user.route('/')
def user_list():
    users = User.query.all()
    print('!!!!', users)
    return render_template('user/users_list.html',
                           users=users
                           )


@user.route('/<int:pk>')
def get_user(pk: int):
    try:
        cur_user = User.query.filter_by(id=pk).one_or_none()
    except KeyError:
        raise NotFound(f'User {pk} is not found')
    return render_template('user/user_details.html',
                           user=cur_user
                           )
