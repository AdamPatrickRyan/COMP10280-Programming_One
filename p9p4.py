##------------------Practical P9Q2----------------##
## 
##User:     Aryan
##DC:       2020-10-15
##DLM:      2020-10-15
##MC:       COMP10280
##SD:       Practical - Factorial
##
##------------------Practical P9Q2----------------## 


##------------------Algorithm----------------------## 


#Get input, check positive, while  counter <= input multiply

##------------------------------------------------## 

#Static values
int_user_input=int(input("Please enter a positive int to check the factorial of that number: "))

if int_user_input==0:
    factorial=1
    print('0! = 1')

elif int_user_input<0:
    print("You entered {} which is less than zero".format(int_user_input))

else:

    #loop allow zero
    while int_user_input>=0:
        #Reset total each loop
        total=1

        for counter in range(1,int_user_input+1):
            total*=counter

        #finish statement
        print("{}! = {}".format(int_user_input,total))
        
        #repeat input
        int_user_input=int(input("Please enter another positive int to check the factorial of that number: "))

    print("You entered {} which is a negative number to end the process.".format(int_user_input))

#Finished