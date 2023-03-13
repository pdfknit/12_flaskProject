from flask import Blueprint, render_template, request, current_app, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound

from forms.article import CreateArticleForm
from models import Article, Author
from models.database import db

article = Blueprint(name='article', import_name=__name__, static_folder='../static', url_prefix='/articles')


@article.route("/")
def articles_list():
    all_articles = Article.query.all()
    one_article = 1
    return render_template("article/articles_list.html", all_articles=all_articles)

#
# @article.route('/<int:pk>')
# def get_article(pk):
#     curr_article = Article.query.filter_by(id=pk).one_or_none()
#     if curr_article is None:
#         raise NotFound
#     return render_template("articles/article_details.html", article=article)


@article.route("/<int:article_id>/")
def article_details(article_id):
    articles = Article.query.filter_by(id=article_id).one_or_none()
    if articles is None:
        raise NotFound
    return render_template("article/details.html", article=articles)

@article.route("/create/", methods=["GET", "POST"], endpoint="create")
@login_required
def create_article():
    error = None
    form = CreateArticleForm(request.form)
    if request.method == "POST":
        current_article = Article(title=form.title.data.strip(), body=form.body.data)
        db.session.add(current_article)
        if current_user.author:
            current_article.author = current_user.author
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            current_article.author = current_user.author
        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create a new article!")
            error = "Could not create article!"
        else:
            return redirect(url_for("article.article_details", article_id=int(current_article.id)))
    return render_template("article/create.html", form=form, error=error)



