from flask import render_template, flash, redirect, session, url_for, request, abort
from flask.ext.login import login_user, logout_user, current_user, login_required
from mturkdb import app
from mturkdb.forms import LoginForm
from mturkdb.models import User

'''
	Home/About/Contact pages and login/logout. 
'''

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if current_user.is_authenticated():
		return redirect(url_for('index'))
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data.lower()).first()
		login_user(user)
		return redirect(url_for('index'))
	return render_template('login.html',form=form)

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))
