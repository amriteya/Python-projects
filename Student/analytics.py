import csv

csv_file_object = csv.reader(open('student.csv','rb'))

count = 0

listOfEvents = []

studentDetails = {}

listOfMissingStudents = []

for row in csv_file_object:
	'''
	if row[4] in listOfEvents:
		continue
	else:
		listOfEvents.append(row[4])
	'''

	if row[2] in studentDetails:
		continue
	else:
		studentDetails[row[2].upper()] = [row[1],row[3]]

	# if row[2] in studentDetails:
	# 	continue
	# else:
	# 	listOfMissingStudents.append(row[2].upper())
	
for student in studentDetails:
	print student,studentDetails[student]
	count = count + 1

print count