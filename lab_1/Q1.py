# Given the following setup {Class, Tally score, Frequency}, develop an application that generates the table shown ; 
# (you can populate the relevant data ; minimum data size :50 records). 
# The table is only an illustration for a data of color scores, you are free to test the application over any data set 
# with the application generating the tally and frequency scores.


import random													# import the required libraries
from tabulate import tabulate

data = []														# store the info about color, freq and tally in a nested list called data

for i in range(50):												# taking 50 colors
	color_name = "color" + str(i+1)								# naming the color as (color + str(i+1))
	freq = random.randint(0, 20)								# randomly generating freq
	t = ""														# initializing empty string to store the tally
	for j in range(1, freq+1):									# loop to obtain the tally
		if(j%5 != 0):											# if the loop iteration is not divisible by 5, then '|'
			t += '|'	
		else:													# else, '\'
			t += "\\"
			t += ' '
	d = [color_name, freq, t]									# prepare a list with the color, freq and tally
	data.append(d)												# append it to data

print(tabulate(data, headers=["Color", "Freq", "Tally"]))		# print the table in a tabular manner
