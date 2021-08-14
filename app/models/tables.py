from app import db

class User(db.Model):
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120))
	email = db.Column(db.String(120), unique=True)
	password = db.Column(db.String(120))

	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
		return True

	@property
	def is_anonymous(self):
		return False

	def get_id(self):
		return str(self.id)

	def __init__(self,name, email, password):
		self.name = name
		self.email = email
		self.password = password

	def __repr__(self):
		return '<User %r>' % self.name


class Post(db.Model):
	__tablename__ = "posts"

	id = db.Column(db.Integer, primary_key=True)
	tittle = db.Column(db.Text, unique=True)
	content = db.Column(db.Text, unique=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	def __init__(self, tittle, content, user_id):
		self.tittle = tittle
		self.content = content
		self.user_id = user_id


	def __repr__(self):
		return '<Post %r>' % self.id 