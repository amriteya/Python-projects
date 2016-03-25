import os

fileOccurence = {}

directoryForSearch = 'E:\Movies'

cwd = os.getcwd()

for (dirname,dirs,files) in os.walk(directoryForSearch):
	print dirs

