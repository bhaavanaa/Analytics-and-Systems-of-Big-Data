# On a given day (average basis), a student is observed to spend 33% of time in studying, 30% in sleeping, 
# 18% in playing, 5% for hobby activities, and rest for spending with friends and family. 
# Plot a pie chart showing his daily activities.


import matplotlib.pyplot as plt 															# import the required lbraries
   
activity = ['studying', 'sleeping', 'playing', 'hobby activities', 'friends and family']	# store the activities in a list
time_spent = [33, 30, 18, 5, 14]															# store the time spent in a list

# piechart
fig = plt.figure(figsize =(10, 7)) 															# size of the chart
plt.pie(time_spent, labels = activity) 														# plot the piechart
plt.title("Daily activities - time distribution")											# title for the plot
plt.show() 																					# display the plot
