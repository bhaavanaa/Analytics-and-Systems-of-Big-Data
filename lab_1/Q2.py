# In a class of 18 students, assume marks distribution in an exam are as follows. 
# Let the roll numbers start with CSE20D01 and all the odd roll numbers secure marks as follows: 25+((i+7)%10) 
# and even roll numbers : 25+((i+8)%10). 
# Develop an application that sets up the data and calculate the mean and median for the marks obtained using the platform support.


marks = []													# initializing an empty list for storing the marks of the 18 students
for i in range(1, 19):										# iterating to obtain their marks
	if(i%2 != 0):		
		marks.append(25+((i+7)%10))							# if odd, then mark = 25+((i+7)%10)
	else:
		marks.append(25+((i+8)%10))							# if even, then mark = 25+((i+8)%10)

print("The marks of the 18 students are - ", marks)			# print the marks of the students

mean = sum(marks)/18										# find the mean of the marks and print it
print("Mean of the marks = ",	 round(mean, 6))

marks.sort()												# sort the list 
median = (marks[8] + marks[9])/2							# find the median of the marks and print it
print("Median of the marks = ", round(median, 6))	