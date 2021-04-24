##------------------Practical P9Q2----------------##
## 
##User:     Aryan
##DC:       2020-10-15
##DLM:      2020-10-15
##MC:       COMP10280
##SD:       Practical - Triangular number
##
##------------------Practical P9Q2----------------## 


##------------------Algorithm----------------------## 


#Get input, check positive, while  counter <= input sum

##------------------------------------------------## 

#Static values
int_user_input=int(input("Please enter a positive int to check the sum of all integers up to that number: "))

if int_user_input==0:
    print('The total is zero')

elif int_user_input<0:
    print("You entered {} which is less than zero".format(int_user_input))

else:

    #loop allow zero
    while int_user_input>=0:
        #Reset counter and total each loop
        counter=0
        total=0

        for counter in range(int_user_input+1):
            total+=counter
            counter+=1

        #finish statement
        print("The sum of all natural numbers up to {} is: {}".format(int_user_input,total))
        
        #repeat input
        int_user_input=int(input("Please enter another positive int to check the sum of all integers up to that number: "))

    print("You entered {} which is a negative number to end the process.".format(int_user_input))

#Finished