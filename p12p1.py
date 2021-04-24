##------------------Practical P12Q1----------------##
## 
##User:     Aryan
##DC:       2020-10-20
##DLM:      2020-10-20
##MC:       COMP10280
##SD:       Practical - Factorial
##
##------------------Practical P12Q1----------------## 


##------------------Algorithm----------------------## 

#0!=1. 

#Define Function for factorial using p11 code.
#Input
##Check input sign, if negative error else fact

##------------------------------------------------## 


def fact(pos_int):
    """Returns the factorial of x for x>=0 int"""
    fact=1

    #multiply fact count
    for i in range(1, pos_int + 1):
        fact*= i

    return fact
        

number = int(input('Enter the number for which you wish to calculate the factorial (an int >= 0):  '))

if number < 0:
    print('Error:  Number entered was less than 0.')
else:
    fact_numb=fact(number)

    print('Factorial of', number, 'is', fact_numb)
        
print('Finished!')