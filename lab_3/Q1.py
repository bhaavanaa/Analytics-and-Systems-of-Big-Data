import statistics

age = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]
    
min_max_normalization = []
z_score_normalization = []
decimal_scaling = []

mean = statistics.mean(age)
std_dev = statistics.stdev(age)

div = 1
while(div < age[len(age)-1]):
    div = div*10

deno = age[(len(age)-1)] - age[0]

for i in range(len(age)):
    min_max_normalization.append(round((age[i]-age[0])/deno, 6))
    z_score_normalization.append(round((age[i]-mean)/std_dev, 6))
    decimal_scaling.append(round(age[i]/div, 6))
    
print("min max normalization : ", min_max_normalization, "\n")
print("z-score normalization : ", z_score_normalization, "\n")
print("normalization by decimal scaling : ", decimal_scaling, "\n")
