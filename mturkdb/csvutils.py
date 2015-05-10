import csv
from models import Attr

'''
	Basically I don't know what csv files look like.

	Design principles (like I'm principled at all):
		each reader should take in a csv file
		and yield a dict of kwargs to pass into a model constructor
		or well, just whatever function calls this stuff
'''

def read_csv(file, lineparser, debug=False, has_header=True):
	header = None
	csvreader = csv.reader(file)
	for row in csvreader:
		if header is None and has_header:
			header = {name.strip():i for i,name in enumerate(row)}
		else:
			for entry in lineparser(row):
				if debug:
					print entry
				yield entry

# attribute file parsers

def quals_parser(row):
	return [{
			'privatename': row[0],
			'amtid': row[1],
			'publicname': row[2],
			'publicdescr': row[3],
			'privatedescr': ''
		}]

def TOSS_key_parser(row):
	'''
		workerid, amtid, value. probably demand a better format?
	'''
	workerid = row[0].strip()
	return [{
				'workerid': workerid,
				'amtid': get_amt_id_from_pubname('Qualification_%02d' % (i+1)),
				'value': int(val) if val else -1
			} for i, val in enumerate(row[1:])]


def get_amt_id_from_pubname(qualname):
	return Attr.query.filter_by(publicname=qualname.title()).first().amtid



