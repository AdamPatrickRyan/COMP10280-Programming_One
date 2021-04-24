##------------------Practical P14Q4----------------##
## 
##User:     Aryan
##DC:       2020-10-22
##DLM:      2020-10-22
##MC:       COMP10280
##SD:       Practical - Prime Exhaustion
##
##------------------Practical P14Q4----------------## 


##------------------Algorithm----------------------## 

#Code from Lecture 13
#for each number in range, check if each number up to range -1 excluding 2 is divisible into number. 
#in each number set up string to capture all pairs
#flag for prime is true
# if div is found, set to false and add factor pair to string 
# Once loop finished print relevant statement.
#once all numbers up to 20 checked we are done.


##------------------------------------------------## 


 #Program to illustrate the use of the else statement on a for loop
 # Search for prime numbers in a range of integers
 # # Look for prime numbers in a range of integers

#checks number from 2 to 20
for number in range(2, 20):

    print(f'Checking {number}: \n')


    #counter to check if prime
    prime_counter=True

    #I want the print statement to allow me to start with ",ab" so include 1number and number1
    print_statement="All pairs of factors are: {}*{}".format(1,number)

    #from 2 up to the number e.g. number=4 for 2,3 try each to check div of 4
    for i in range(2, number):

        #check if number is divisible by each number up to number-1
        if number % i == 0:
            factor=int(number/i)
            print_statement+=', {}*{}'.format(i,factor) #i first to go smallest to largest
            prime_counter=False

    #not prime
    if prime_counter==False:
        print_statement+=', {}*{}.\n\n'.format(number,1) #Add the final

    #prime
    else:
        print_statement='{} is prime! \n\n'.format(number)

    print(print_statement)

print('Finished!')