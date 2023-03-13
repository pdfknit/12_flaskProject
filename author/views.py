from flask import Blueprint, render_template
from models import Author

authors = Blueprint(name='authors', import_name=__name__, static_folder='../static', url_prefix='/authors')


@authors.route("/", endpoint="list")
def authors_list():
    authors = Author.query.all()
    return render_template("author/list.html", authors=authors)
