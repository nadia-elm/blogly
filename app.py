from flask import Flask,request,redirect,render_template,flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db,User



app = Flask(__name__)
app.app_context().push()


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:secret@localhost:5432/blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY']='SECRET'
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


connect_db(app)
db.create_all()


@app.route('/')
@app.route('/users')
def users_list():
    """Display a list of users"""

    users = User.query.all()
    return render_template('users.html',users = users)


@app.route('/users/new', methods=['GET','POST'])
def add_new_user():
    if request.method == 'POST':
        first = request.form['F']
        last = request.form['L']
        image= request.form['image']

        # create new user
        new_user = User(first_name= first, last_name= last, image_url= image  or None)
        db.session.add(new_user)
        # commit to db
        db.session.commit()

        flash('new user added ', 'success')

        return redirect("/users")
    return render_template('add_user_form.html')



@app.route('/users/<int:user_id>')
def user_details(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user_details.html', user = user)


@app.route('/users/<int:user_id>/edit', methods=['GET','POST'])
def edit_user(user_id):
        if request.method == 'POST':
            # get the user from db
            user = User.query.get_or_404(user_id)
            # update user info
            user.first_name = request.form['first_name']
            user.last_name = request.form['last_name']
            user.image_url= request.form['image_url']
            db.session.add(user)
            # commit to db
            db.session.commit()

            flash('user updated ', 'success')

            return redirect("/users")
        user = User.query.get_or_404(user_id)
        return render_template('edit.html',user = user)


@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    flash('user deleted', 'danger')

    return redirect('/users')




   
   
