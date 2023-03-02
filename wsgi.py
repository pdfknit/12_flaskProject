from app import create_app
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
