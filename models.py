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
    posts = db.relationship('Post')
    



class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.Text, nullable = False)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime,  default=datetime.datetime.now)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
    user = db.relationship('User')
   
