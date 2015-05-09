from flask import render_template, redirect, url_for
from mturkdb import app, lm, utils
from mturkdb.forms import AddUserForm
from mturkdb.models import User


'''
	Admin functions.

	TODO:
		edit users. revoke access etc. play god!!!
		oh, i guess better database error handling.
		wait should worker management (or views) really only be an admin thing?
'''


@app.route('/admin/manageusers')
@utils.admin_required
def manage_users(): 
	return render_template('admin/manageusers.html', userlist=User.query.order_by(User.name),
		add_user_form = AddUserForm())

@app.route('/admin/adduser', methods=['GET','POST'])
@utils.admin_required
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





