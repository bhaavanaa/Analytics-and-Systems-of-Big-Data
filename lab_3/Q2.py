### QUESTION 2 - Use the given dataset and perform the operations listed below.


import csv													# import the required libraries
import math
import numpy as np


with open("Avocado_Dataset.csv", 'r') as f:					# open the dataset in read mode
    data = list(csv.reader(f, delimiter = ","))				# read the dataset into the variable data


## a) Sort the attribute “Total Volume” in the given dataset and distribute the data into equal sized/frequency bins. 
## Let the number of bins be 250. Smooth the sorted data by (i)bin-means, (ii) bin-medians, (iii) bin-boundaries

tvol = [] 													# initialize list to store the total volume column
for i in range(1, len(data)):								# convert the elements under the total volume column to float
	tvol.append(float(data[i][2]))

total_volume = np.array(tvol) 								# convert the list to float
total_volume = np.sort(total_volume)						# sort the total_volume

no_of_bins = 250											# given that the no. of bins is 250
bin_size = math.ceil(len(total_volume) / no_of_bins)		# so, bin size can be found by total no. of elements / no. of bins

bin1 = np.zeros((no_of_bins, bin_size)) 					# create bin1 for mean
bin2 = np.zeros((no_of_bins, bin_size)) 					# create bin2 for median
bin3 = np.zeros((no_of_bins, bin_size)) 					# create bin3 for boundaries
 
for i in range (0, no_of_bins*bin_size, bin_size): 			# bin mean
	k = int(i/bin_size)   									# required for storing the index of the bin
	mean = sum(total_volume[i:i+bin_size])/bin_size   		# obtaining the mean of the elements present in the bin                
	for j in range(bin_size): 								# replace the elements of the bin with the mean 
		bin1[k,j] = round(mean, 6) 
print("Bin Mean: \n",bin1) 									# print the mean bin
	
for i in range (0, no_of_bins*bin_size, bin_size):			# bin median
	k = int(i/bin_size) 									# required for storing the index of the bin
	for j in range (bin_size): 								# replace the elements of the bin with the median
		bin2[k,j] = total_volume[i+math.floor(bin_size/2)] 	# compute the median
print("Bin Median: \n",bin2)								# print the median bin

for i in range (0, no_of_bins*bin_size, bin_size):			# bin boundaries 
	k = int(i/bin_size) 									# required for storing the index of the bin
	for j in range (bin_size): 								# replace the elements of the bin with the closest boundary element
		if (total_volume[i+j]-total_volume[i]) < (total_volume[i+bin_size-1]-total_volume[i+j]): 
			bin3[k,j] = total_volume[i] 					# if the element is closer to the start element
		else: 
			bin3[k,j] = total_volume[i+bin_size-1]	 		# if the element is closer to the last element
print("Bin Boundaries: \n",bin3) 							# print the boundaries bin


## b) The dataset represents weekly retail scan data for National retail volume (units) and price. 
## However, the company is interested in knowing the monthly (total per month) and annual sales (total per year),
## rather than the total per week. So, reduce the data accordingly.

date = data[1][0][-7:]  									# for obtaining the month-year from date column - first date of dataset
region = data[1][12] 										# for obtaining region - first region of dataset
c = 0														# for count - calculation of avg price per month

list_date = []												# initialize the required lists
list_avg_price = []
list_total_volume = []
list_4046 = []
list_4225 = []
list_4770 = []
list_total_bags = []
list_small_bags = []
list_large_bags = []
list_xlarge_bags = []
list_region = []

sum_avg_price = 0 											# initialize the sum variables to zero
sum_total_volume = 0
sum_4046 = 0
sum_4225 = 0
sum_4770 = 0
sum_total_bags = 0
sum_small_bags = 0
sum_large_bags = 0
sum_xlarge_bags = 0

for i in range(1, len(data)):
	if(date == data[i][0][-7:] and region == data[i][12]):		# if the month-year and region match with initialized values
		d = data[i][1]											# for checking if the avg_price is float or Nan
		if(d.replace('.', '', 1).isdigit() == True):
			sum_avg_price += float(data[i][1])					# if float - add to the sum_avg_price, else ignore that cell
			c += 1												# and increment the count 
		sum_total_volume += float(data[i][2])					# update the respective sum values
		sum_4046 += float(data[i][3])
		sum_4225 += float(data[i][4])
		sum_4770 += float(data[i][5])
		sum_total_bags += float(data[i][6])
		sum_small_bags += float(data[i][7])
		sum_large_bags += float(data[i][8])
		sum_xlarge_bags += float(data[i][9])
	else:														# if month-year doesnt match with the initialized values
		list_date.append(date) 									# append the computed data to the list initialized 
		if(c != 0):												# if all values of avg_price is Nan
			list_avg_price.append(sum_avg_price/c)				# avg price is coputed
		else:
			list_avg_price.append(0)							# else avg_price for the month = 0
		list_total_volume.append(sum_total_volume)				# append the other computed sums to the respective lists
		list_4046.append(sum_4046)
		list_4225.append(sum_4225)
		list_4770.append(sum_4770)
		list_total_bags.append(sum_total_bags)
		list_small_bags.append(sum_small_bags)
		list_large_bags.append(sum_large_bags)
		list_xlarge_bags.append(sum_xlarge_bags)
		list_region.append(region)
		date = data[i][0][-7:]									# initilaize the modified values, as it is different from previous one
		region = data[i][12]
		d = data[i][1]
		if(d.replace('.', '', 1).isdigit() == True):
			sum_avg_price = float(data[i][1])
			c = 1
		else:
			sum_avg_price = 0
			c = 0
		sum_total_volume = float(data[i][2])
		sum_4046 = float(data[i][3])
		sum_4225 = float(data[i][4])
		sum_4770 = float(data[i][5])
		sum_total_bags = float(data[i][6])
		sum_small_bags = float(data[i][7])
		sum_large_bags = float(data[i][8])
		sum_xlarge_bags = float(data[i][9])
			
print("Date 	avg_price 	total_volume 	4046 	4225 	4770 	total_bags 	small_bags 	large_bags 	xlarge_bags 	list_region")
for i in range(len(list_date)):
	print(list_date[i], "	", round(list_avg_price[i], 2), "	", round(list_total_volume[i], 2), "	", round(list_4046[i], 2), "	", 
		round(list_4225[i], 2), "	", round(list_4770[i], 2), "	", round(list_total_bags[i], 2), "	", round(list_small_bags[i], 2), "	", 
		round(list_large_bags[i], 2), "	", round(list_xlarge_bags[i], 2), "	", list_region[i])
# print(len(list_date))

## c) Summarize the number of missing values for each attribute

col0 = 0													# initialize the count for all columns to 0								
col1 = 0
col2 = 0
col3 = 0
col4 = 0
col5 = 0
col6 = 0
col7 = 0
col8 = 0
col9 = 0
col10 = 0
col11 = 0
col12 = 0

for i in range(1, len(data)):
	d0 = data[i][0]											# store the required values for checking if the string is float
	d1 = data[i][1]
	d2 = data[i][2]
	d3 = data[i][3]
	d4 = data[i][4]
	d5 = data[i][5]
	d6 = data[i][6]
	d7 = data[i][7]
	d8 = data[i][8]
	d9 = data[i][9]
	if(d0 == ''):											# if the values are not available, incerement count for that column
		print(d0)
		col0+=1
	elif(d1 == '' or d1.replace('.', '', 1).isdigit() == False):
		col1+=1
	elif(d2 == '' or d2.replace('.', '', 1).isdigit() == False):
		col2+=1
	elif(d3 == '' or d3.replace('.', '', 1).isdigit() == False):
		col3+=1
	elif(d4 == '' or d4.replace('.', '', 1).isdigit() == False):
		col4+=1
	elif(d5 == '' or d5.replace('.', '', 1).isdigit() == False):
		col5+=1
	elif(d6 == '' or d6.replace('.', '', 1).isdigit() == False):
		col6+=1
	elif(d7 == '' or d7.replace('.', '', 1).isdigit() == False):
		col7+=1
	elif(d8 == '' or d8.replace('.', '', 1).isdigit() == False):
		col8+=1
	elif(d9 == '' or d9.replace('.', '', 1).isdigit() == False):
		col9+=1
	elif(data[i][10] == ''):
		col10+=1
	elif(data[i][11].isdigit() == False):
		col11+=1
	elif(data[i][12] == ''):
		col12+=1

print("The count of the missing values are-")				# print the final counts for the columns
print("Date - ", col0)
print("Averge price - ", col1)
print("Total volume - ", col2)
print("4046 - ", col3)
print("4225 - ", col4)
print("4770 - ", col5)
print("Total bags - ", col6)
print("Small bags - ", col7)
print("Large bags - ", col8)
print("XLarge bags - ", col9)
print("Type - ", col10)
print("Year - ", col11)
print("Region - ", col12)


## d) Populate data for the missing values of the attribute= “Average Price” by averaging 
## all the values of the “Avg Price” attribute that fall under the same “REGION” attribute value.
can = 0
for i in range(1, len(data)):								# for every row in data
	d = data[i][1]
	if(data[i][1] == '' or d.replace('.', '', 1).isdigit() == False):	# if it is missing value
		s = 0												# to keep track of the sum 
		count = 0											# to keep track of the count for finding the avg value
		for j in range(1, len(data)):						
			d = data[j][1]									# used for checking if it is a float value or no
			if(data[j][12] == data[i][12] and d.replace('.', '', 1).isdigit() == True):		# if it is a float value
				s = s + float(data[j][1])					# add it to the sum variable
				count+=1									# increment the count
		data[i][1] = str(round(s/count, 6))					# find avg and replace the missing value
	if(i<30):
		print(data[i])													# print the modified data

 
## e) Discretize the attribute= “Date” using concept hierarchy into {Old, New, Recent}
## (Consider 2015,2016 : Old, 2017: New, 2018: Recent).

for i in range(1, len(data)):								# for every row of data
	if((data[i][11] == '2015') or (data[i][11] == '2016')):	# 2015 or 2016 - Old
		data[i][0] = "Old"
	elif(data[i][11] == '2017'):							# 2017 - New
		data[i][0] = "New"
	elif(data[i][11] == '2018'):							# 2018 - Recent
		data[i][0] = "Recent"
	# print(data[i])													# print the updated data

