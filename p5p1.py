##------------------Practical 5 HW3----------------##
## 
##User:     Aryan
##DC:       2020-10-06
##DLM:      2020-10-06
##MC:       COMP10280
##SD:       Negative check
##
##------------------Practical 5 HW3----------------## 

##------------------Algorithm----------------------## 

#Get input, check if negative.

##------------------------------------------------## 


input_value=input("Please enter an integer to check if negative: ")

#Not checking if valid entry per Brightspace comment
int_user_input=int(input_value)

if int_user_input<0:
    print('You entered {} which is negative'.format(int_user_input))