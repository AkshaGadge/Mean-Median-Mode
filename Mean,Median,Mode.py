#---------------------------------------------
#Python program to Print Mean of the Elements.
n_num = [1,2,3,4,5]
n = len(n_num)
get_sum = sum(n_num)
mean = get_sum/n
print("given list:",n_num)
print("mean/Average is :",int(mean))
#Alternate
import statistics
print("mean/Average is :",statistics.mean(n_num))

#Output =
# mean/Average is : 3
# mean/Average is : 3
#----------------------------------------------
#Python program to Print Median of the Elements.
n_num = [1,2,3,4,5]
n = len(n_num)
n_num.sort()
if n % 2 == 0:
    median1 = n_num[n//2]
    median2 = n_num[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = n_num[n//2]
print("Median is:",median)
#alternate way
import statistics
print("Median is:",statistics.median(n_num))

#Output =
# Meddian is: 3
# Median is: 3
#--------------------------------------------
#Python program to Print Mode of the Elements.
import statistics
set1 = [1,2,3,3,4,4,4,5,5,5,5]
print("Given list is:",set1)
print("mode of given list:",statistics.mode(set1))

#Output =
# Given list is: [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5]
# mode of given list: 5
#--------------------------------------------------




