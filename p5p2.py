##------------------Practical 5 HW3----------------##
## 
##User:     Aryan
##DC:       2020-10-06
##DLM:      2020-10-06
##MC:       COMP10280
##SD:       Negative or Non-Negative check
##
##------------------Practical 5 HW3----------------## 

##------------------Algorithm----------------------## 

#Get input, check if negative or non-negative.

##------------------------------------------------## 


input_value=input("Please enter an integer to check if negative or non-negative: ")

#Not checking if valid entry per Brightspace comment
int_user_input=int(input_value)

if int_user_input>=0:
    print('You entered {} which is non-negative'.format(int_user_input))

else:
    print('You entered {} which is negative'.format(int_user_input))