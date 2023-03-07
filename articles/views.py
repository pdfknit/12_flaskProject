from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

ARTICLES = {
    1: 'Статья 1',
    2: 'Статья 1',
    3: 'Статья 1',
}
article = Blueprint(name='article', import_name=__name__, static_folder='../static', url_prefix='/articles')


# USERS = ['Alice', 'Vlad', 'Sonya']


@article.route('/')
def articles_list():
    return render_template('article/articles_list.html',
                           articles=ARTICLES
                           )


@article.route('/<int:pk>')
def get_article(pk: int):
    try:
        title = ARTICLES[pk]
    except KeyError:
        raise NotFound(f'Article {pk} is not found')
    return render_template('article/article_details.html',
                           title=title
                           )
