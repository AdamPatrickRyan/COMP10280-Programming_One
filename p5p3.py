##------------------Practical 5 HW3----------------##
## 
##User:     Aryan
##DC:       2020-10-06
##DLM:      2020-10-06
##MC:       COMP10280
##SD:       Negative, zero, or positive float check
##
##------------------Practical 5 HW3----------------## 

##------------------Algorithm----------------------## 

#Get input, check if negative, zero or positive 

##------------------------------------------------## 


input_value=input("Please enter a number to check if negative, zero or positive: ")

#Not checking if valid entry per Brightspace comment
float_user_input=float(input_value)

if float_user_input>0:
    print('You entered {} which is positive'.format(float_user_input))

elif float_user_input==0:
    print('You entered {} which is zero'.format(float_user_input))

else:
    print('You entered {} which is negative'.format(float_user_input))