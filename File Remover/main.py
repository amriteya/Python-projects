import os
import shutil
from collections import OrderedDict
from operator import itemgetter


cwd = os.getcwd();
#print cwd

DIRECTORY = ""

if not os.path.exists(DIRECTORY):
	os.makedirs(DIRECTORY)

extensionsDirectory = {}

for (dirname,dirs,files) in os.walk("C:\\"):
	for filename in files:
		extension = filename.split('.')[-1]
		if len(extension) < 10:
			#print extension
			if extensionsDirectory.has_key(extension):
				extensionsDirectory[extension] += 1
			else:
				extensionsDirectory[extension] = 1
		
max = 0

for key in extensionsDirectory.keys():
	if max < extensionsDirectory[key]:
		max = extensionsDirectory[key]
		print max
	# if extensionsDirectory[key] > 2:
	# 	print key+' : '+str(extensionsDirectory[key])


'''
for (dirname,dirs,files) in os.walk('C:\\'):
	print "Working in "+dirname
	for filename in files:
		extension = filename.split('.')[-1]
		if extension == "mp3":
			try:
				shutil.move(dirname+"\\"+filename,DIRECTORY+filename)
				print "Moved File "+filename
			except:
				print dirname+"\\"+filename
'''