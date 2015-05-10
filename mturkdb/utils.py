from flask import render_template
from flask.ext.login import current_user
from models import User, Attr, WorkerAttr
from mturkdb import app, db, lm
import csvutils
from functools import wraps
from random import random #testing testing

# TODO: check buncha errors
# everything is probably an upsert. actually, who knows. but uhh figure out how to upsert.

@lm.user_loader
def load_user(id):
	return User.query.get(id)

@app.errorhandler(403)
def err_403(e):
	return render_template('403.html'), 403

@app.errorhandler(401)
def err_401(e):
	return render_template('401.html'), 401

def admin_required(fn):
	@wraps(fn)
	def admin_fn(*args, **kwargs):
		if current_user.is_authenticated() and current_user.is_admin():
			return fn(*args, **kwargs)
		else:
			return lm.unauthorized()
	return admin_fn


def add_new_user(name, email, password, descr, isadmin):
	new_user = User(name=name, email=email, pwdhash=password, 
		descr=descr, isadmin=isadmin)
	db.session.add(new_user)
	db.session.commit()
	return True

def add_new_attribute(publicname, privatename,
		publicdescr, privatedescr, amtid, single=False):
	# let's assume that each new attribute is a separate transaction.
	# i mean it's not like people are going to upload a gazillion at once.
	# right chrystal?? :<

	if amtid=='':
		success, amtid = add_attr_to_mturk(publicname, publicdescr)
		if not success:
			return success
	new_attr = Attr(amtid=amtid, publicname=publicname,
		privatename=privatename, publicdescr=publicdescr, privatedescr=privatedescr)
	db.session.add(new_attr)
	if single:
		db.session.commit()
	return True

def add_attrs_from_csv(bulkfile):

	line_generator = csvutils.read_csv(bulkfile, lineparser=csvutils.quals_parser,
		debug=False)
	failures = []
	for line_dict in line_generator:
		success = add_new_attribute(**line_dict)
		if not success:
			failures.append(line_dict)
	db.session.commit()
	return True, failures

def add_worker_attribute(workerid, amtid, value, grant_qual=False, single=False):

	if grant_qual:
		success = grant_qual_in_mturk(workerid, amtid, value)
		if not success:
			return success
	new_worker_attr = WorkerAttr(workerid=workerid, amtid=amtid, value=value)
	db.session.add(new_worker_attr)
	if single:
		db.session.commit()
	return True

def add_worker_attributes(bulkfile, grant_quals):

	line_generator = csvutils.read_csv(bulkfile, debug=False,lineparser=csvutils.TOSS_key_parser)
	failures = []
	for line_dict in line_generator:
		success = add_worker_attribute(**line_dict)
		if not success:
			failures.append(line_dict)
	db.session.commit()
	return True, failures


# TODO: CELERY

def add_attr_to_mturk(name, descr):
	print 'Bunny'
	return True, 'FooBar' + str(random())[-5:]

def grant_qual_in_mturk(workerid, amtid, value):
	if value < 0:
		value = None
	print 'Bunny'
	return True
	