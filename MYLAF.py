
import os
import shutil

def makeFolder(folder):
	if not os.path.exists(folder):
		os.makedirs(folder)


def MYLAF(root):
	makeFolder(root)
	makeFolder(root+'/MYLAF')
	# chatRecord
	makeFolder(root+'/MYLAF/chatRecord')
	# CODE
	makeFolder(root+'/MYLAF/CODE')
	makeFolder(root+'/MYLAF/CODE/project')
	makeFolder(root+'/MYLAF/CODE/repo')
	makeFolder(root+'/MYLAF/CODE/study')
	makeFolder(root+'/MYLAF/CODE/template')
	# DATA
	makeFolder(root+'/MYLAF/DATA')
	makeFolder(root+'/MYLAF/DATA/image')
	makeFolder(root+'/MYLAF/DATA/video')
	makeFolder(root+'/MYLAF/DATA/other')
	# DOCUMENT
	makeFolder(root+'/MYLAF/DOCUMENT')
	makeFolder(root+'/MYLAF/DOCUMENT/Note')
	makeFolder(root+'/MYLAF/DOCUMENT/Paper')
	makeFolder(root+'/MYLAF/DOCUMENT/Book')
	# rebuild
	makeFolder(root+'/MYLAF/rebuild')
	# SOFTWARE
	makeFolder(root+'/MYLAF/SOFTWARE')
	# VIRTUALMACHINE
	makeFolder(root+'/MYLAF/VIRTUALMACHINE')

	# own
	shutil.copy('MYLAF.py', root+'/MYLAF')

	return True

root_dir = input('MYLAF ROOT Directory:')
MYLAF(root_dir)
