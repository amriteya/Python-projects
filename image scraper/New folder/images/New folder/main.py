import urllib

for count in range(38,70):
	urllib.urlretrieve(""+str(count)+".jpg",str(count)+".jpg")
	print count


# http://viralboom.com/wp-content/uploads/2015/11/img561-17700.gif