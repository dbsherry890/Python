from app import app
from website import db
from website.models import User

with app.app_context():

    user = User(email="norshy@gmail.com",
                password="password1", first_name="Norsh")
    db.session.add(user)
    db.session.commit()
