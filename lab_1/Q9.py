# Consider the following sample of weights for 75 individuals: 79 71 89 57 76 64 82 82 67 80 81 65 73 79 79
# 60 58 83 74 68 78 80 78 81 76 65 70 76 58 82 59 73 72 79 87 63 74 90 69 70 83 76 61 66 71 60 57 81 57 65 81
# 78 77 81 81 63 71 66 56 62 75 64 74 74 70 71 56 69 63 72 81 54 72 91 92. 
# For the above data generate histograms and depict them using packages in your platform. 
# Explore the different types of histograms available and test drive the types supported in your platform.


from matplotlib import pyplot as plt 							# import the required library

weights = [79, 71, 89, 57, 76, 64, 82, 82, 67, 80,				# store the weights of the individuals in a list
			 81, 65, 73, 79, 79, 60, 58, 83, 74, 68,
			 78, 80, 78, 81, 76, 65, 70, 76, 58, 82,
			 59, 73, 72, 79, 87, 63, 74, 90, 69, 70,
			 83, 76, 61, 66, 71, 60, 57, 81, 57, 65, 
			 81, 78, 77, 81, 81, 63, 71, 66, 56, 62,
			 75, 64, 74, 74, 70, 71, 56, 69, 63, 72, 
			 81, 54, 72, 91, 92]

fig, ax = plt.subplots(figsize =(10, 7)) 						# set the size of the plot
ax.hist(weights)												# plot the histogra for the weights
plt.xlabel("weights")											# set the x axis label as weights
plt.ylabel("frequency")											# set the y axis label as frequency
plt.title("Histrogram for the weights of 75 individuals")		# give a title to the plot
plt.show()														# display the plot

plt.hist(weights,bins=20, color='#0504aa',alpha=0.7,rwidth=0.85,histtype='barstacked')
plt.show() 

plt.hist(weights,bins=20, color='#0504aa',alpha=0.7,rwidth=0.85,histtype='bar',label='blue')
plt.show() 

plt.hist(weights,bins=220, color='#0504aa',alpha=0.7,rwidth=0.85,histtype='stepfilled',label='blue')
plt.show() 

plt.hist(weights,bins=20, color='#0504aa',alpha=0.7,rwidth=0.85,histtype='step',label='blue')
plt.show()