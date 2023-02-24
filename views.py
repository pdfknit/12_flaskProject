from flask import Blueprint, render_template
from constants import ARTICLES, USERS

main_page = Blueprint(name='main_page', import_name=__name__, static_folder='../static', url_prefix='')


@main_page.route('/')
def main():
    return render_template('/base.html',
                           articles=ARTICLES, users=USERS
                           )
