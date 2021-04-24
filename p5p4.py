##------------------Practical 5 HW3----------------##
## 
##User:     Aryan
##DC:       2020-10-06
##DLM:      2020-10-06
##MC:       COMP10280
##SD:       Ranges of value
##
##------------------Practical 5 HW3----------------## 

##------------------Algorithm----------------------## 

#Get input, check which range it's in. If not in first move to second etc. finish by negative.

##------------------------------------------------## 


input_value=input("Please enter a number to check what range it's in: ")

#Not checking if valid entry per Brightspace comment
int_user_input=int(input_value)

#Group maximums
max_range_g1=0
max_range_g2=20
max_range_g3=40
max_range_g4=60
max_range_g5=80
max_range_g6=100


#Group 1 - 0
if int_user_input==max_range_g1 :
    print('Number is equal {}'.format(int_user_input))

#Group 2 - 0 to 20
elif max_range_g1<int_user_input<=max_range_g2:
    print("Number is greater than {} and less than or equal to {}".format(max_range_g1,max_range_g2))

#Group 3 - 20 to 40
elif max_range_g2<int_user_input<=max_range_g3:
    print("Number is greater than {} and less than or equal to {}".format(max_range_g2,max_range_g3))

#Group 4 - 40 to 60
elif max_range_g3<int_user_input<=max_range_g4:
    print("Number is greater than {} and less than or equal to {}".format(max_range_g3,max_range_g4))

#Group 5 - 60 to 80
elif max_range_g4<int_user_input<=max_range_g5:
    print("Number is greater than {} and less than or equal to {}".format(max_range_g4,max_range_g5))

#Group 6 - 80 to 100
elif max_range_g5<int_user_input<=max_range_g6:
    print("Number is greater than {} and less than or equal to {}".format(max_range_g5,max_range_g6))

 #Group 7 - 100+
elif int_user_input>max_range_g6:
    print('Number is greater than {}'.format(max_range_g6))

#Group 0 - Less than 0
else:
    print('You entered {} which is less than {}'.format(int_user_input,max_range_g1))