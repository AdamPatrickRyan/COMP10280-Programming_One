##------------------Practical 7 HW4----------------##
## 
##User:     Aryan
##DC:       2020-10-08
##DLM:      2020-10-08
##MC:       COMP10280
##SD:       Triangular number
##
##------------------Practical 7 HW4----------------## 

##------------------Algorithm----------------------## 

#Take N\{0} as the set
#Set a counter, limit, and cumulative total
#once the counter hits the limit get the current cumulative value 
#Done

#

##------------------------------------------------## 

#Static values

limit=5000
count=1
running_total=0
#test_case=((limit)*(limit+1))/2

#include limit to sum first 50
while count<=limit:
    running_total+=count

    if count==limit:
        #Technically redundant as running_total=sum_value at this step but nice for safety
        sum_value=running_total

    count+=1

print(f'The sum of the numbers 1 to {limit} is: {sum_value}')

#######CODE BELOW IS A TEST CASE - not asked to be part of program so commented out##########

#if test_case==sum_value:
#    print(f'The sum of the numbers 1 to {limit} is: {sum_value}')
#
#else:
    #something went wrong
#    print('You have an error somewhere - check your code')




#Wikipedia has no check on postivity