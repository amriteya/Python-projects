import urllib

for count in range(38,70):
	urllib.urlretrieve(""+str(count)+".jpg",str(count)+".jpg")
	print count
