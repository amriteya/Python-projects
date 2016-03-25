yourList = ['0','1','2','3','4','5','6','7','8','9']
for x in xrange(97,123):
	yourList.append(chr(x))

print yourList

newList = []

for x in yourList:
	for y in yourList:
		newList.append(x+y)


# print newList

for i in xrange(2):
	passwordList = []
	for x in yourList:
		for y in newList:
			passwordList.append(x+y)
	newList = passwordList
	print passwordList
