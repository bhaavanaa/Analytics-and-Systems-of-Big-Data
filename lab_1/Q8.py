# Extend the application developed in (7) to support relative grading which uses the class average (mean) and
# standard deviation to compute the cutoffs for various grades as opposed to fixing them statically; 
# you can refer the sample grader (excel sheet) attached to understand the formulas for fixing the cutoffs; 
# the grader would involve, mean, standard deviation, max mark, passed students data mean, etc. 
# Understand the excel 	grader thoroughly before you try mimicking such an application in your development platform.


import random									# import the required libraries
import statistics
import collections

mid_sem=[]										# initialize the lists for storing the marks and grades
end_sem=[]
assignments=[]
grades=[]
total=[]

for i in range(0,20):							# iterate for all the students
	m = random.randint(0,31)					# randomly generate an int in (0, 30) for midsem marks
	mid_sem.append(m)				
	e = random.randint(0,51)					# randomly generate an int in (0, 50) for endsem marks				
	end_sem.append(e)					
	a = random.randint(0,21)					# randomly generate an int in (0, 20) for assignment marks
	assignments.append(a)
	s = mid_sem[i] + end_sem[i] + assignments[i] 	# find the total marks of the student
	total.append(s)

mean = statistics.mean(total) 					# obtain the mean of the toal marks
pass_min = mean/2 								# set the pass as mean/2									

no_passed = 0 									# to keep count of the number of students who have passed
pass_total = 0 									# to store the sum of total marks of passed students

for i in range(0,20): 							# iterating over every student
	if(total[i] > pass_min): 					# if their total > pass mark, then pass
		no_passed = no_passed + 1				# increment the count for passed students
		pass_total = pass_total + total[i]      # add the marks of the passed student to get the sum of marks of students who passed

pass_stud_mean = pass_total / no_passed 		# stores the mean of the passed marks
max_total = max(total) 							# stores the highest mark

X = pass_stud_mean - pass_min
S_grade = max_total - 0.1*(max_total - pass_stud_mean) # mark for S grade
Y = S_grade - pass_stud_mean

A_grade = pass_stud_mean + (Y*5/8)				# mark for A grade
B_grade = pass_stud_mean + (Y*2/8)				# mark for B grade
C_grade = pass_stud_mean - (X*2/8)				# mark for C grade
D_grade = pass_stud_mean - (X*5/8)				# mark for D grade

print("passing cutoff :","\nS grade: ", S_grade, "\nA grade: ", A_grade, "\nB grade: ", B_grade, "\nC grade: ", C_grade, "\nD grade: ", D_grade, "\n")

for i in range(0, 20):							# iterate for all students and assigning their grade as per the obtained conditions
	if(total[i] > S_grade):
		grades.append('S')
	elif(total[i] > A_grade):
		grades.append('A')
	elif(total[i] > B_grade):
		grades.append('B')
	elif(total[i] > C_grade):
		grades.append('C')
	elif(total[i] > D_grade):
		grades.append('D')
	elif(total[i] > pass_min):
		grades.append('E')

print("Total marks ",total);					# print the required values
print("Grades      ",grades, "\n")

elements_count = {}

elements_count = collections.Counter(grades)
for key, value in elements_count.items(): 
    print (key, value)