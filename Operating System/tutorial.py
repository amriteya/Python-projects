import os
from ID3 import *
import csv

f = open('SongsList.csv','wb')

songsList = []
temp = []

directoryForSearch = 'C:/'

writer = csv.writer(f)
writer.writerow(('ALBUM', 'COMMENT', 'ARTIST', 'TITLE', 'YEAR', 'GENRE'))
count = 0

for (dirname, dirs, files) in os.walk(directoryForSearch):
   for filename in files:
       if filename.endswith('.mp3'):
       	   # print filename
           theFile = os.path.join(dirname,filename)
           try:
           		audiofile = ID3(theFile)
           		if len(audiofile.values()) == 5:
	           		writer.writerow(audiofile.values())
           		temp = audiofile.values()
           		temp.append(theFile)
           		songsList.append(temp)
           		# print temp
           		# print type(audiofile.values())
           except:
           		print ''
           		# print 'Could not load info for file',filename

           # print os.path.getsize(theFile)/1024*1024,theFile.encode('utf-8')
           count = count + 1

f.close()

for songs in songsList:
	if len(songs) == 5:
		for s in songsList:
			try:
				if songs[0] == s[0] and songs[1] == s[1] and songs[2] == s[2] and songs[3] == s[3] and songs[4] != s[4]:
					print s[4]
					print songs[4]
					break
			except:
				print 'error'
	# for songs in songs:
	# 	for s in songs:
	# 		if songs['TITLE']

print 'Files:', count