import csv

'''
	Basically I don't know what csv files look like.

	Design principles (like I'm principled at all):
		each reader should take in a csv file
		and yield a dict of kwargs to pass into a model constructor
		or well, just whatever function calls this stuff
'''

def read_csv(file, lineparser, debug=False):
	header = None
	csvreader = csv.reader(file)
	for row in csvreader:
		if header is None:
			header = {name.strip():i for i,name in enumerate(row)}
			if debug:
				print header
		else:
			yield lineparser(header, row)

# attribute file parsers

def TOSS_key_parser(header, row):
	return {
			'privatename': row[header['Variable Name']],
			'amtid': row[header['Qualification ID']],
			'publicname': row[header['Qualification Name']],
			'publicdescr': row[header['Qualification Description']],
			'privatedescr': ''
		}




