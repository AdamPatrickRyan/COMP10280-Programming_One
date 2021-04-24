##------------------Practical P14Q3----------------##
## 
##User:     Aryan
##DC:       2020-10-22
##DLM:      2020-10-22
##MC:       COMP10280
##SD:       Practical - Prime Exhaustion
##
##------------------Practical P14Q3----------------## 


##------------------Algorithm----------------------## 

#Code from Lecture 13
#for each number in range, check if each number up to range -1 excluding 2 is divisible into number. If not prime. Proof by exhaustion.

##------------------------------------------------## 


 #Program to illustrate the use of the else statement on a for loop
 # Search for prime numbers in a range of integers
 # # Look for prime numbers in a range of integers

#checks number from 2 to 20
for number in range(2, 20):

    #from 2 up to the number e.g. number=4 for 2,3 try each to check div of 4
    for i in range(2, number):

        #check if number is divisible by each number up to number-1
        if number % i == 0:
            print(number, 'equals', i, '*', number//i)

            #Found a factor not prime
            break
    else:
        # loop fell through without finding a factor
        print(number, 'is a prime number')

print('Finished!')