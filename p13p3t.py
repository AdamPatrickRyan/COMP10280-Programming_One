##------------------Practical P13Q3----------------##
## 
##User:     Aryan
##DC:       2020-10-20
##DLM:      2020-10-20
##MC:       COMP10280
##SD:       Practical - Max Function from Lecture 15 again
##
##------------------Practical P13Q3----------------## 


##------------------Algorithm----------------------## 


 
 #Program to print out the largest of two numbers entered by the user
 # # Uses two functions:  
 # max and print_max
 # def print_max():
 # """Function that prints out the largest of two numbers
 # 
 # Uses the function max to find the largest"""
 # def max(a, b):
 # """Function that returns the largest of its two arguments"""
 # if a > b:
 # return a
 # else:
 # return b
 # 
 # 
 # # Prompt the user for two numbers
 # number1 = float(input(’Enter a number:  ’))
 # 
 # number2 = float(input(’Enter a number:  ’))
 # 
 # print(’The largest of’, number1, ’and’, number2,’is’, max(number1, number2))
 # 
 # returnprint_max()

 #print max function with inner max function
 ##two inputs
 ##compare and print

 ###How it works:
 #The max function is scoped interally in print max
 #max works as in previous problems.

 #Within print_max, two inputs are requested
 #theres a print statement that prints the max
#an empty return is passed so nothing is actually passed from the function, only the interior print ststement gets shown to user.

#calling the function runs it (i.e. asks for input, gets max from inner function, prints the statement, returns none)

##------------------------------------------------## 


 #Program to print out the largest of two numbers entered by the user
 #Uses two functions:  max and print_max
def print_max():
    """Function that prints out the largest of two numbers

    Uses the function max to find the largest"""

    def max(a, b):
        """Function that returns the largest of its two arguments"""
        if a > b:
            return a
        else:
            return b
 
    #Prompt the user for two numbers
    number1 = float(input('Enter a number:  '))
    number2 = float(input('Enter a number:  '))
 
    print('The largest of', number1, 'and', number2,'is', max(number1, number2))
 
    return

###The following is for the text part:

def test_case_1():
    "What happens if you include line print(print_max())"
    try:
        print(print_max())

        #return print valid in python3.8
        return print(f"""It has a {type(print(print_max()))} so returns an empty print statement as print_max returns nothing""")

    except:
        return print("This should not cause error")

def test_case_2():
    "What happens if you call print_max"

    try:
        print_max

        return print(f"""The funtcion accepts no arguments so should run""")

    except:
        return print(f"""This should not cause error""")


def test_case_3():
    "What happens if you call print(print_max)"
    
    try:
        print(print_max)

        #return print valid in python3.8
        return print(f"""It has a NoneType so returns an empty print statement as print_max returns nothing""")

    except:
        return print("This should not cause error")

def test_cases():
    test_case_1()
    test_case_2()
    test_case_3()
    return

#test_cases()

test_case_1()