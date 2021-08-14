from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user
from app import app, db, lm

from app.models.tables import User, Post
from app.models.forms import LoginForm, PostForm


@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route("/index")
@app.route("/")
def index():
	post4 = []
	for i in reversed(range(100)):
		post = Post.query.filter_by(id=i).first()
		if post != None:
			post4.append(post)
			global data
			data = post4
	return render_template("index.html", post1=data)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email = form.email.data).first()
		if user and user.password == form.password.data:
			login_user(user)
			print(login_user(user))
			flash("Logged In.")
			return redirect(url_for("index"))
		else:
			flash("Invalid Login ")
	return render_template("login.html", form=form)

@app.route("/logout")
def logout():
	logout_user()
	flash("logout")
	print("logout")
	return redirect(url_for("login"))

@app.route("/edit/<id>", methods=['GET', 'POST'])
def edit(id):
	update = Post.query.filter_by(id=id).first()
	editPost = PostForm()
	if editPost.validate_on_submit():
		editPost = Post.query.filter_by(id=id).first()
		#print(editPost.tittle.data)
		editPost.tittle = request.form['tittle']
		editPost.content = request.form['content']
		db.session.add(editPost)
		db.session.commit()
		flash("Poste updeted.")
		return redirect(url_for("index"))
	return render_template("edit.html", editPost=editPost, update=update)


@app.route("/create", methods=['GET', 'POST'])
def create():
	createPost = PostForm()
	if createPost.validate_on_submit():
		tittle = createPost.tittle.data
		content = createPost.content.data
		creates = Post(tittle, content, "1")
		db.session.add(creates)
		db.session.commit()
		flash("Poste created.")
		return redirect(url_for("index"))
	return render_template("create.html", createPost=createPost)

@app.route("/delete/<id>")
def delete(id):
	delt = Post.query.filter_by(id=id).first()
	db.session.delete(delt)
	db.session.commit()
	flash("Poste Deleted.")
	return redirect(url_for('index'))

@app.route("/add_user")
def add_user():
	user = User("admin", "admin@gmail.com", "admin123")
	db.session.add(user)
	db.session.commit()
	return "OK"