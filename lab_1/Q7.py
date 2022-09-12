# Develop an application (absolute grader) that accepts marks scored by 20 students in ASBD course 
# (as a split up of three : Mid Sem (30), End Sem(50) and Assignments(20). 
# Compute the total and use it to grade the students following absolute grading : >=90 – S ; >=80 – A and so on till D. 
# Compute the Class average for total marks in the course and 50% of class average would be fixed as the cut off for E. 
# Generate a frequency table for the grades as well (Table displaying the grades and counts of them).


import random												# import the required libraries
from tabulate import tabulate

data = []													# a nested list to store the details of students
final_marks = []											# stores the total marks of the student

for i in range(20):											# for every student present in the class
	name = "student" + str(i+1)								# name of the student
	midsem = random.randint(0, 30)							# random generated midsem marks
	endsem = random.randint(0, 50)							# random generated endsem marks
	assignments = random.randint(0, 20)						# random generated assignment marks
	total = midsem + endsem + assignments 					# total marks = midsem + endsem + assignments
	final_marks.append(total)								# appending the total marks of the student to the list		
	d = [name, midsem, endsem, assignments, total]			# creating a list for student details
	data.append(d)											# appending the details of the student to the data list

class_avg = sum(final_marks)/20								# calculating class average and printng it
print("The class average is ", class_avg, "\n")				

grades = []													# list to store the grades obtained by students
count = [0, 0, 0, 0, 0, 0, 0]								# count of the students who obtained a particular grade

for i in range(20):											# for every student, assign the grade
	if(final_marks[i] >= 90):								# assigning S grade given the condition, appending the grade to the student details 
		data[i].append('S')
		grades.append('S')
		count[0] += 1										# incerementing the count for S grade
	elif(final_marks[i] >= 80):								# assigning A grade given the condition, appending the grade to the student details
		data[i].append('A')
		grades.append('A')
		count[1] += 1										# incerementing the count for A grade
	elif(final_marks[i] >= 70):								# assigning B grade given the condition, appending the grade to the student details
		data[i].append('B')
		grades.append('B')
		count[2] += 1										# incerementing the count for B grade		
	elif(final_marks[i] >= 60):								# assigning C grade given the condition, appending the grade to the student details
		data[i].append('C')
		grades.append('C')							
		count[3] += 1										# incerementing the count for C grade
	elif(final_marks[i] >= 50):								# assigning D grade given the condition, appending the grade to the student details
		data[i].append('D')
		grades.append('D')
		count[4] += 1										# incerementing the count for D grade
	elif(final_marks[i] >= int(class_avg/2)):				# assigning E grade if total is greater than half of class avg, appending the grade to the student info
		data[i].append('E')
		grades.append('E')
		count[5] += 1										# incerementing the count for E grade
	else:													# assigning U grade given the condition, appending the grade to the student details								
		data[i].append('U')
		grades.append('U')
		count[6] += 1										# incerementing the count for U grade

print(tabulate(data, headers=["Name", "Midsem", "Endsem", "Assignments", "Total", "Grade"]))		# print the data of the students

print("\n\nGrade 		No. of students")					# print the grade and freq table
print("S 		", count[0])
print("A 		", count[1])
print("B 		", count[2])
print("C 		", count[3])
print("D 		", count[4])
print("E 		", count[5])
print("U 		", count[6])
