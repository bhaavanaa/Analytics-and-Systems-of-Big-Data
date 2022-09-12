# For a sample space of 20 elements, the values are fitted to the line Y=2X+3, X>5. 
# Develop an application that sets up the data and computes the standard deviation of this sample space. 
# (use random number generator supported in your development platform to generate values of X).


import random																	# import the required libraries
import statistics

x = []																			# create empty lists for storing the x and y values
y = []
for i in range(0, 20):															# iterating 20 times to genrate the x values and find the y values
	r = random.randint(0, 100)													# generate random no. between x and y
	x.append(r)																	# append the random no. to x
	y.append(2*r+3)																# find the corresponding y value and append to the list
print("The values of x are - ", x)												# print the x and y values
print("The values of y are - ", y)

std_dev = statistics.stdev(y)													# find the std dev. of the sample space i.e. y
print("The standard deviation of the sample space = ", round(std_dev, 6))		# print the std dev.