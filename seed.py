from models import User,db
from app import app



# Create all tables
db.drop_all()
db.create_all()

User.query.delete()
    
    

# create some users
bublina = User(first_name = 'bublina', last_name='sparky',image_url="https://images.unsplash.com/photo-1522069169874-c58ec4b76be5?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8ZmlzaHxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=800&q=60")
blue = User(first_name = 'blue', last_name='the cat',image_url="https://images.unsplash.com/photo-1495360010541-f48722b34f7d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1036&q=80")
stevie =User(first_name = 'stevie', last_name='chick',image_url="https://images.unsplash.com/photo-1589050593767-a754dd738587?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTZ8fGNoaWNrZW58ZW58MHx8MHx8&auto=format&fit=crop&w=800&q=60")
tamy = User(first_name = 'tammy', last_name='the tiger',image_url= "https://images.unsplash.com/photo-1615824996195-f780bba7cfab?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8dGlnZXJ8ZW58MHx8MHx8&auto=format&fit=crop&w=800&q=60")
tommy = User(first_name = 'Tommy', last_name='the turtle',image_url= "https://images.unsplash.com/photo-1568660357733-823cbddb0f6a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8dHVydGxlfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60")

db.session.add_all([bublina, blue, stevie, tamy, tommy])
db.session.commit()