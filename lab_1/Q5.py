# In Analytics and Systems of Bigdata course, for a class of 100 students, 
# around 31 students secured ‘S’ grade, 29 secured ‘B’ grade, 25 ‘C’ grades, and rest of them secured ‘D’ grades. 
# If the range of each grade is 15 marks. (S for 85 to 100 marks, A for 70 to 85 ...). 
# Develop an application that represents the above data : using Pie and Bar graphs.


import matplotlib.pyplot as plt 									# import the required lbraries
   
grade = ['S', 'A', 'B', 'C', 'D']									# store the grades in a list
no_of_students = [31, 0, 29, 25, 15]								# store the no. of students who got that grade in a list

# piechart
fig = plt.figure(figsize =(10, 7)) 									# size of the chart
plt.pie(no_of_students, labels = grade) 							# plot the piechart
plt.title("Grade distribution")										# title for the plot
plt.show() 															# display the plot
   
# bar graph   
fig = plt.figure(figsize = (10, 5))   								# size of the chart
plt.bar(grade, no_of_students, color ='maroon',  width = 0.8) 		# plot the bar graph
plt.xlabel("Grades") 												# label the x-axis
plt.ylabel("No. of students") 										# label the y-axis
plt.title("Grade distribution") 									# title for the plot
plt.show() 															# display the plot
