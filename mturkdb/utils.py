from flask import render_template
from models import User
from mturkdb import app, db, lm

@lm.user_loader
def load_user(id):
	return User.query.get(id)

@app.errorhandler(403)
def err_403(e):
	return render_template('403.html'), 403

@app.errorhandler(401)
def err_401(e):
	return render_template('401.html'), 401


def add_new_user(name, email, password, descr, isadmin):
	# TODO: check db error
	new_user = User(name=name, email=email, pwdhash=password, 
		descr=descr, isadmin=isadmin)
	db.session.add(new_user)
	db.session.commit()
	return True