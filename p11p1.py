##------------------Practical P11Q1----------------##
## 
##User:     Aryan
##DC:       2020-10-15
##DLM:      2020-10-15
##MC:       COMP10280
##SD:       Practical - Factorial
##
##------------------Practical P11Q1----------------## 


##------------------Algorithm----------------------## 

#0!=1. Everything else is original code from Lecture_1

##------------------------------------------------## 



print_originalcodeis=f"""
number = int(input(’Enter the number for which you wishto calculate the factorial (an int >= 0):  ’))

if number < 0:
    print('Error:  Number entered was less than 0.')

    else:
        if number == 0:
            fact = 1
        elif number == 1:
            fact = 1
        else:
            fact = 1

            for i in range(1, number + 1):
                fact*= i
        print('Factorial of', number, 'is', fact)
        
    print('Finished!')"""

number = int(input('Enter the number for which you wish to calculate the factorial (an int >= 0):  '))

if number < 0:
    print('Error:  Number entered was less than 0.')
else:
    fact = 1

    for i in range(1, number + 1):
        fact*= i

    print('Factorial of', number, 'is', fact)
        
print('Finished!')