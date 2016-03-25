import urllib
regNo = ""
websiteLink = ""

for count in range(1,267):
	count = str(count);
	if len(count) < 3:
		while(len(count) != 3):
			count = "0"+count
	urllib.urlretrieve(websiteLink+"?rgno="+regNo+count, regNo+count+".jpg")