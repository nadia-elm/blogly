from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


default_image ="https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png" 


class User(db.Model) :
    __tablename__ = "users"  

    id = db.Column(db.Integer, primary_key = True, autoincrement = True) 
    first_name = db.Column(db.String(50), nullable = False)
    last_name = db.Column(db.String(50))
    image_url = db.Column(db.String, default = default_image)