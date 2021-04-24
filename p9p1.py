##------------------Practical P9Q1----------------##
## 
##User:     Aryan
##DC:       2020-10-15
##DLM:      2020-10-15
##MC:       COMP10280
##SD:       Practical - Triangular number
##
##------------------Practical P9Q1----------------## 


##------------------Algorithm----------------------## 


#Get input, check positive, while  counter <= input sum

##------------------------------------------------## 

#Static values
int_user_input=int(input("Please enter a positive to check the sum of all integers up to that number: "))

if int_user_input==0:
    print('The total is zero')

elif int_user_input<0:
    print("You entered {} which is less than zero".format(int_user_input))

else:
    counter=0
    total=0

    #loop
    while counter<=int_user_input:
        total+=counter
        counter+=1

    print("The sum of all natural numbers up to {} is: {}".format(int_user_input,total))


