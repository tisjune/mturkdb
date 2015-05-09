from flask.ext.wtf import Form 
from models import User
from wtforms import TextField, BooleanField, PasswordField, SubmitField
from wtforms.validators import Required, Email

class LoginForm(Form):
	email = TextField('Email', 
		[Required('Please enter your email address.'), 
		Email('Please enter a valid email address.')])
	password = PasswordField('Password', 
		[Required('Please enter your password.')])
	submit = SubmitField('Log in')

	def validate(self):
		if not Form.validate(self):
			return False

		user = User.query.filter_by(email = self.email.data.lower()).first()
		if user and user.check_password(self.password.data):
			return True
		else:
			self.email.errors.append("Invalid email or password")
			return False

class AddUserForm(Form):
	email = TextField('Email', 
		[Required('Please enter user\'s email address.'), 
		Email('Please enter a valid email address.')])
	name = TextField('Name')
	password = PasswordField('Initial Password', 
		[Required('Please enter a password.')])
	descr = TextField('Description')
	isadmin = BooleanField('Grant admin privileges', default=False)
	submit = SubmitField('Add User')

	def validate(self):
		if not Form.validate(self):
			return False
		user = User.query.filter_by(email = self.email.data.lower()).first()
		if user:
			self.email.errors.append("That email is already taken")
			return False
		else:
			return True