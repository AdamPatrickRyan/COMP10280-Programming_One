##------------------Practical P10Q1----------------##
## 
##User:     Aryan
##DC:       2020-10-15
##DLM:      2020-10-15
##MC:       COMP10280
##SD:       Practical - SquareRoot
##
##------------------Practical P10Q1----------------## 


##------------------Algorithm----------------------## 


#Check if >=0
#if so:
# loop through everything up to the number entered
#square them check if square is equal to number, if yes thats the root and exit
#if loop is over then not perfect square


##------------------------------------------------## 

import sys

#Static values
int_user_input=int(input("Please enter a positive number to find its integer square root: "))

if int_user_input>=0:
    for k in range(int_user_input+1):
        k_sq=k**2

        if k_sq==int_user_input:
            print("{} is a perfect square, with a root of {}.".format(int_user_input,k))
            sys.exit()
    
    print("{} is not a perfect square.".format(int_user_input))

else:
    print('You entered a negative number.') #if negative than square root is not an element of Z -> not integer square root.
