##------------------Practical P12Q3----------------##
## 
##User:     Aryan
##DC:       2020-10-20
##DLM:      2020-10-20
##MC:       COMP10280
##SD:       Practical - Approx Sqr Root
##
##------------------Practical P12Q3----------------## 


##------------------Algorithm----------------------## 

#Define Function for square root - Code from lecture 12
#tolerance define and ask input.
#check sign
#run function

##------------------------------------------------## 

#Lecture 12 Code:
# Finding the square root of a number
# # Program prompts the user for the number
# # Uses exhaustive enumeration to find an approximate solution
# epsilon = 0.01
# step = epsilon**2
# numGuesses = 0# 
# Prompt the user for a number
# number = float(input('Enter the number for which you wishto calculate the square root:  '))
# root = 0.0
# 
# while abs(number - root**2) >= epsilon and root**2 <= number:

# root += stepnum
# Guesses += 1

# if numGuesses % 100000 == 0:
# print('Still running.  Number of guesses:', numGuesses)
# 
# print('Number of guesses:', numGuesses)
# if abs(number - root**2) < epsilon:
# print('The approximate square root of', number, 'is', root)
# else:print('Failed to find a square root of', number)
# print('Finished!')

def sqr_root(number,tolerance):
    step = tolerance**2
    numGuesses = 0 
    root = 0.0
 
    while abs(number - root**2) >= tolerance and root**2 <= number:
        root += step
        numGuesses += 1

        if numGuesses % 100000 == 0:
            print('Still running.  Number of guesses:', numGuesses)

    print('Number of guesses:', numGuesses)

    if abs(number - root**2) < tolerance:
        
        if root**2==number:
            #exact
            print('The square root of', number, 'is', root)
        else:
            #approximate
            print('The approximate square root of', number, 'is', root)

        return root

    else:
        return print('Failed to find a square root of', number)
 
    print('Finished!')  
        

number = float(input('Enter the number for which you wish to calculate the square root (>=0):  '))
#tol = int(input('Enter the tolerance (>=0):  '))
tol=0.01 #tolerance from lecture

if number < 0:
    print('Error:  Number entered was negative.')
else:
    #>0
    sqr_root_num=sqr_root(number,tol)

    #type=float found, else print statement
    if type(sqr_root)==float:
        print("The square root of", number, "is", sqr_root_num)
    
    
        
print('Finished!')