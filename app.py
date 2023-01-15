from flask import Flask,request,redirect,render_template,flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db,User,Post,Tag,PostTag



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



# adding posts functionality
@app.route('/users/<int:user_id>/posts/new', methods=['GET','POST'])
def user_posts(user_id):
    if request.method == 'POST':
        user = User.query.get_or_404(user_id)
        tag_ids = [int(num) for num in request.form.getlist('tags')]
        tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()
        post = Post(title = request.form['title'], content= request.form['content'],user = user, tags = tags)
        db.session.add(post)
        db.session.commit()

        flash('post created', 'success')
    
      
        posts= user.posts
        
        return render_template('user_details.html', user = user, posts = posts)
   
    user = User.query.get(user_id)
    posts= user.posts
    tags = Tag.query.all()
    return render_template('create_post.html', user = user, posts = posts, tags = tags)



@app.route('/posts/<int:post_id>')
def show_post(post_id):
    post = Post.query.get(post_id)
    user= User.query.filter_by(id= post.user_id)
    return render_template('post.html', post=post, user = user)



@app.route('/posts/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)

    db.session.delete(post)
    db.session.commit()

    flash('post deleted', 'danger')

    return redirect(f"/users/{post.user_id}")


@app.route('/posts/<int:post_id>/edit', methods=['GET', 'POST'])
def edit_post(post_id):
    if request.method == 'POST':
         # get post from db
        post = Post.query.get_or_404(post_id)
         # update post
        post.title = request.form['title'] 
        post.content = request.form['content']

        tag_ids = [int(num) for num in request.form.getlist('tags')]
        tags = Tag.query.filter(Tag.id.in_(tag_ids)).all() 
         
        db.session.add(post)
        # commit to db
        db.session.commit()

        flash('post updated ', 'success')

        return redirect(f"/users/{post.user_id}")

    post = Post.query.get_or_404(post_id)
    user= User.query.filter_by(id= post.user_id)
    tags= Tag.query.all()

    return render_template('edit_post.html',user = user, post = post,tags =tags)


   
@app.route('/tags')
def show_tags():
    tags = Tag.query.all()
    return render_template('tags.html', tags = tags)


@app.route('/tags/new', methods=['GET', 'POST'])
def new_tag():
    if request.method == 'POST':
        name = request.form['tag']

        new_tag = Tag(name = name)
        db.session.add(new_tag)
        db.session.commit()
        flash('tag added', 'success')
        return redirect('/tags')

    return render_template('create_tag.html')


@app.route('/tags/<int:tag_id>')
def tag_details(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    return render_template('tag_details.html', tag = tag)



@app.route('/tags/<int:tag_id>/delete', methods=['POST'])
def delete_tag(tag_id) :
    tag = Tag.query.get_or_404(tag_id)

    db.session.delete(tag)
    db.session.commit()

    flash('tag deleted', 'danger')

    return redirect('/tags')


@app.route('/tags/<int:tag_id>/edit',methods=['GET', 'POST'])
def edi_tag(tag_id):
    if request.method == 'POST':
        tag = Tag.query.get_or_404(tag_id)
        tag.name = request.form['tag']
        db.session.add(tag)
        db.session.commit()
        flash('tag updated ', 'success')
        return redirect('/tags')

    
    tag = Tag.query.get_or_404(tag_id)
    return render_template('/edit_tag.html',tag = tag)









