import os

from app import create_app
from models import User
from models.database import db

app = create_app()


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('Created!!!!!!!')


@app.cli.command("create-users")
def create_users():
    from models import User
    admin = User(username="admin", is_staff=True, email="admin@admin.ru")
    user_01 = User(username="sofia", email="sofia@gmail.com")
    db.session.add(admin)
    db.session.add(user_01)
    db.session.commit()
    print("created users ", admin, user_01)


@app.cli.command("create-admin")
def create_admin():
    """
    Run in your terminal:
    ➜ flask create-admin
    > created admin: <User #1 'admin'>
    """
    admin = User(username="admin", is_staff=True)
    admin.password = os.environ.get("ADMIN_PASSWORD") or "admin"
    db.session.add(admin)
    db.session.commit()
    print("created admin:", admin)


@app.cli.command("create-tags")
def create_tags():
    from models import Tag

    for name in [
        "flask",
        "django",
        "python",
        "sqlalchemy",
        "news",
    ]:
        tag = Tag(name=name)
        db.session.add(tag)
    db.session.commit()
    print("created tags")
