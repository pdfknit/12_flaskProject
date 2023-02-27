from flask import Blueprint, render_template

from auth.views import login_manager
from constants import ARTICLES, USERS
from models import User
from user.views import get_user

main_page = Blueprint(name='main_page', import_name=__name__, static_folder='../static', url_prefix='')



@main_page.route('/')
def main():
    curr_user = 0
    return render_template('/base.html',
                           articles=ARTICLES, users=USERS, curr_user=curr_user,
                           )
