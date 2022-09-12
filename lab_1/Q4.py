# For a given data of heights of a class, the heights of 15 students are recorded as 
# 167.65, 167, 172, 175, 165, 167, 168, 167, 167.3, 170, 167.5, 170, 167, 169, and 172. 
# Develop an application that computes; explore if there are any packages supported in your platform that depicts these measures / their calculation 
# of central tendency in a visual form for ease of understanding.
# a. Mean height of the student
# b. Median and Mode of the sample space
# c. Standard deviation
# d. Measure of skewness. [(Mean-Mode)/standard deviation]


import statistics																				# import the required library
import seaborn as sns
from matplotlib import pyplot as plt

heights = [167.65, 167, 172, 175, 165, 167, 168, 167, 167.3, 170, 167.5, 170, 167, 169, 172]	# store the heights in a list

mean = statistics.mean(heights)																	# compute the mean using statistics lib
median = statistics.median(heights)																# compute the median using statistics lib
mode = statistics.mode(heights)																	# compute the mode using statistics lib
std_dev = statistics.stdev(heights)																# compute the std dev. using statistics lib
skewness = (mean - mode)/std_dev																# compute the skewness = (Mean-Mode)/standard deviation

print("Mean of the heights = ", round(mean, 6))													# print the values computed
print("Median of the heights = ", round(median, 6))
print("Mode of the heights = ", round(mode, 6))
print("Std dev. of the heights = ", round(std_dev, 6))
print("Skewness of the heights = ", round(skewness, 6))

sns.displot(heights, kde=True, rug=True)
plt.axvline(median, color='b', linestyle='-')
plt.axvline(mean, color='g', linestyle='-')
plt.axvline(mode, color='r', linestyle='-')
plt.show()