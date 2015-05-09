from flask import render_template, flash, redirect, session, url_for, request
from flask.ext.login import current_user, login_required
from mturkdb import app, lm, utils
from mturkdb.forms import AddUserForm
from mturkdb.models import User
from functools import wraps

'''
	Admin functions.
'''

def admin_required(fn):
	@wraps(fn)
	def admin_fn(*args, **kwargs):
		if current_user.is_authenticated() and current_user.is_admin():
			return fn(*args, **kwargs)
		else:
			return lm.unauthorized()
	return admin_fn


@app.route('/admin/manageusers')
@admin_required
def manage_users(): 
	return render_template('admin/manageusers.html', userlist=User.query.order_by(User.name),
		add_user_form = AddUserForm())

@app.route('/admin/adduser', methods=['GET','POST'])
@admin_required
def add_users():
	form = AddUserForm()
	if form.validate_on_submit():
		result = utils.add_new_user(form.name.data, form.email.data, form.password.data, 
				form.descr.data, form.isadmin.data)
		if result:
			return redirect(url_for('manage_users'))
		else:
			form.email.errors.append("Error: user add unsuccessful")
	return render_template('admin/manageusers.html', add_user_form=form, 
		userlist=User.query.order_by(User.name))




