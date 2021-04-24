##------------------Practical P13Q4----------------##
## 
##User:     Aryan
##DC:       2020-10-20
##DLM:      2020-10-20
##MC:       COMP10280
##SD:       Practical - Scoping from Lecture 15
##
##------------------Practical P13Q4----------------## 


##------------------Algorithm----------------------## 


 
#Program to illustrate scoping in Python
# def f(x):
# """Function that adds 1 to its argument and prints it out"""
# print('In function f:')
# 
# x += 1
# y = 1
# print('x is', x)
# print('y is', y)
# print('z is', z)
# return x
# 
# x, y, z = 5, 10, 15
# print('Before function f:')
# print('x is', x)
# print('y is', y)
# print('z is', z)
# z = f(x)
# print('After function f:')
# print('x is', x)
# print('y is', y)
# print('z is', z)

#function gets defined.
#xyz


##------------------------------------------------## 

def f(x):
    """Function that adds 1 to its argument and prints it out"""
    print('In function f: ')

    #x defined as input and then redefined internally as input + 1
    x += 1

    #y defined in scope of function as 1
    y = 1
    print('x is', x)
    print('y is', y)

    #z not defined in function but outside is 15
    print('z is', z)

    return x #input+1

x, y, z = 5, 10, 15
#defined variable xyz


#will return these
print('Before function f: ')
print('x is', x)
print('y is', y)
print('z is', z)

#in function x gets defined as input+1, y inside function is defined as 1, z unaltered,
z = f(x) #z gets redefined, y value of 1 gets tossed after function, x value inside function of x+1 gets tossed.

#x outside was unchanged, y outside was unchanged, in functions disposed of, z was value of function return which was x+1
print('After function f: ')
print('x is', x)
print('y is', y)
print('z is', z)