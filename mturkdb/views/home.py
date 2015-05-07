from flask import render_template, flash, redirect, session, url_for, request, abort
from mturkdb import app

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')