from flask.ext.wtf import Form 
from models import User, Attr
from wtforms import TextField, BooleanField, PasswordField, SubmitField, FileField
from wtforms.validators import Required, Email, regexp
from werkzeug import secure_filename

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

class AddAttributeForm(Form):
	publicname = TextField('Public Name')
	privatename = TextField('Private Name')
	publicdescr = TextField('Public Description')
	privatedescr = TextField('Private Description')
	amtid = TextField('MTurk Qualification ID (leave blank to create a new qual)',
		[Required('Not a feature yet okay???')])
	submit = SubmitField('Add Attribute')

	def validate(self):
		if not Form.validate(self):
			return False
		attr = Attr.query.filter_by(amtid = self.amtid.data.lower()).first()
		if attr:
			self.amtid.errors.append("That qualification already exists. To edit it, do uhh something.")
			return False
		else:
			return True

class BulkAttributeForm(Form):
	bulkfile = FileField('CSV File', 
		[Required('Please upload a csv file')])
	submit = SubmitField('Add Attributes')

	def validate(self):
		# TODO: UHHH....WTF 
		# (it's not like anyone is going to hack this but still)
		# WTFORMS YOU SUCK
		return Form.validate(self)

class BulkWorkerForm(Form):
	bulkfile = FileField('CSV File',
		[Required('Please upload a csv file')])
	grantquals = BooleanField('Grant quals to everyone', default=False)
	submit = SubmitField('Add Workers')

	def validate(self):
		# again...wtf, wtforms
		return Form.validate(self)








