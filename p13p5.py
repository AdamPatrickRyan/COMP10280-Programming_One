

##------------------Practical P13Q5----------------##
## 
##User:     Aryan
##DC:       2020-10-20
##DLM:      2020-10-20
##MC:       COMP10280
##SD:       Practical - Practical - Scoping from Lecture 15 again - try catch to show local/global
##
##------------------Practical P13Q5----------------## 


##------------------Algorithm----------------------## 


 
#Program to illustrate scoping in Python

#define a,b,c 
#show x,y,z, don't exist

#function takes an input
#show as no local assignment a,b,c read from ext
#show values as local var get created, by using excepts to show not yet defined.
#define values and show they now exist
#show a,b,c untouched

#reassign c as output of function

#show a,b,c exist and c is reassigned but xyz no longer exist by using an except (technicslly it only shows at least one don't exist but no point using a try catch for each when they'll all return the catch).




##------------------------------------------------## 

def f(x):
    """Function that adds 1 to its argument and prints it out"""
    print("\n\nIn function f: ")

    print(f"In f, the values of a,b,c are read from exterior as {a},{b},{c}")

    #x defined as input and then redefined internally as input + 1

    #Initial value
    print(f"The input is: {x}")
    x += 1

    #x now is x=x+1
    print(f"x has been reassigned: {x}")

    #show x,y,z have no values yet as local so force catch to show
    try:
        print(f"The value of y is: {y}")
    except:
        print('Except in f line 71: y is not yet assigned')

    try:
        print(f"The value of z is: {z}")
    except:
        print('Except in f line 76: z is not yet assigned')
    

    #y = a^2 +2a + 1 = (a+1)^2
    y = (a+1)**2
    print(f"The value of y now is defined and is: {y}")

    z=x

    #defined using global var.
    z=c**2

    #if i redefine or assign a/b/c will fail as now will expect local assignment
    print(f"The value of z now is defined c**2.")

    #all adjustments done show all values
    print('x is', x)
    print('y is', y)
    print('z is', z)
    print('a is', a)
    print('b is', b)
    print('c is', c)

    return x #whatever x in function is defined as (input+1)

a, b, c = 5, 10, 15
#defined variable xyz


#will return these
print('Before function f: ')
print('a is', a)
print('b is', b)
print('c is', c)

#show that x,y,z not defined yet by forcing catch
try:
    print('x is', x)
    print('y is', y)
    print('z is', z)

except:
    print('Except pre-f line 118: x,y,z not defined yet -> Only defined inside f')

#assign value of new_var_z f(a)
c = f(c) 

#x globally was unchanged, y globally was unchanged, z was value of function return which was x+1
print('\n\nAfter function f: ')

#untouched
print('a is', a)
print('b is', b)

#c has been redefined as the return of x in the function
print('c is', c)

try:
    print('x is', x)
    print('y is', y)
    print('z is', z)
except:
    print("Except after  f line 138: x,y,z no longer exist / don't exist outside function")

#I'm not really sure what we're meant to do in this question or what's required so I've changed out the variables/function and added purposely breaking sttements
#I don't see a good way of really demonstrating without using try/catch which even though is not covered yet in the lecture seems the most obvious/best way of showing this?