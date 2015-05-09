from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
from mturkdb import db

class User(db.Model):
	__tablename__ = 'Users'

	id = db.Column(db.Integer(), primary_key = True)
	name = db.Column(db.String(100))
	email = db.Column(db.String(120), unique=True, nullable=False)
	pwdhash = db.Column(db.String(66), nullable=False)
	isadmin = db.Column(db.Boolean(), default=False)
	descr = db.Column(db.String(500))
	awskey = db.Column(db.String(100))
	awssecretkey = db.Column(db.String(100)) # todo: how long are these things actually 

	def __init__(self, **kwargs):
		super(User, self).__init__(**kwargs)
		self.set_password(kwargs['pwdhash'])
		self.email = kwargs['email'].lower()
		self.name = kwargs['name'].title()

	def set_password(self, password):
		self.pwdhash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.pwdhash, password)

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def is_admin(self):
		return self.isadmin 

	def get_id(self):
		return unicode(self.id)

	def __repr__(self):
		return '<User %d; name=%r; email=%r>' % (self.id, self.name, self.email)  

class Worker(db.Model):
	__tablename__ = 'Workers'

	workerid = db.Column(db.String(100), primary_key=True)

	def __init__(self, **kwargs):
		super(Attr, self).__init__(**kwargs)
		self.workerid = kwargs['workerid'].lower()

	def __repr__(self):
		return '<Worker %r>' % (self.workerid)

class Attr(db.Model):
	__tablename__ = 'Attrs'

	amtid = db.Column(db.String(100), primary_key=True)
	publicname = db.Column(db.String(100))
	privatename = db.Column(db.String(100))
	publicdescr = db.Column(db.String(500))
	privatedescr = db.Column(db.String(500))

	def __init__(self, **kwargs):
		super(Attr, self).__init__(**kwargs)
		if kwargs['privatename'] == '':
			self.privatename = self.publicname
		if kwargs['privatedescr'] == '':
			self.privatedescr = self.publicdescr
		self.amtid = kwargs['amtid'].upper()


	def __repr__(self):
		return '<Attribute mturk=%r name=%r descr=%r>' % (
						self.amtid, self.privatename, self.privatedescr)

class WorkerAttr(db.Model):
	__tablename__ = 'WorkerAttrs'

	workerid = db.Column(db.String(100), db.ForeignKey('worker.workerid'), 
					primary_key=True)
	amtid = db.Column(db.Integer(), db.ForeignKey('attr.amtid'), 
					primary_key=True)
	value = db.Column(db.Integer())
	granted = db.Column(db.Boolean())

	def __init__(self, **kwargs):
		super(Attr, self).__init__(**kwargs)
		self.amtid = kwargs['amtid'].lower()
		self.workerid = kwargs['workerid'].lower()

	def __repr__(self):
		return 'Worker: %r; Attribute: %r, Value: %r, Granted: %r' % (self.workerid,
			self.attrid, self.value, self.granted)

class Action(db.Model):
	__tablename__ = 'Actions'

	id = db.Column(db.Integer(), primary_key=True)
	userid = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
	descr = db.Column(db.String(500))













