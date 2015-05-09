from flask import render_template, flash, redirect, session, url_for, request
from flask.ext.login import current_user, login_required
from mturkdb import app, utils
from mturkdb.forms import AddAttributeForm, BulkAttributeForm
from mturkdb.models import Attr 
from werkzeug import secure_filename

'''
	Functions for viewing and managing attributes.

	Note that attributes right now are equivalent to qualifications.

	TODO:
		think about whether that's the right choice.
		hook everything up to mturk (with vegetables??)
		access controls on attributes? again choice.
		error handling??
		FEEDBACK!!!
'''

@app.route('/attributes')
@utils.admin_required
def manage_attributes():
	return render_template('attributes.html', 
		add_attr_form=AddAttributeForm(),
		bulk_attr_form=BulkAttributeForm(),
		attrlist = Attr.query.order_by(Attr.privatename))

@app.route('/attributes/addattribute', methods=['GET','POST'])
@utils.admin_required
def add_attribute():
	form = AddAttributeForm()
	if form.validate_on_submit():
		result = utils.add_new_attribute(form.publicname.data,
			form.privatename.data, form.publicdescr.data,
			form.privatedescr.data, form.amtid.data)
		if result:
			return redirect(url_for('manage_attributes'))
		else:
			form.submit.errors.append('Error: unable to add attribute')
	return render_template('attributes.html', add_attr_form=form,
		bulk_attr_form=BulkAttributeForm(),
		attrlist = Attr.query.order_by(Attr.privatename))

@app.route('/attributes/bulkaddattribute', methods=['GET','POST'])
@utils.admin_required
def bulk_add_attrs():
	form = BulkAttributeForm()
	if form.validate_on_submit():
		if request.method == 'POST':
			bulkfile = request.files['bulkfile']
			result,failures = utils.add_attrs_from_csv(bulkfile)
			# TODO: handle failures
			if result:
				return redirect(url_for('manage_attributes'))
			else:
				form.submit.errors.append('Error: failed to read file')
	return render_template('attributes.html', 
		add_attr_form=AddAttributeForm(),
		bulk_attr_form=form,
		attrlist = Attr.query.order_by(Attr.privatename))




