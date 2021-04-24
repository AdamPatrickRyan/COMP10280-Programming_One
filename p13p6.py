

##------------------Practical P13Q5----------------##
## 
##User:     Aryan
##DC:       2020-10-20
##DLM:      2020-10-20
##MC:       COMP10280
##SD:       Practical - Recursion factorial
##------------------Practical P13Q5----------------## 


##------------------Algorithm----------------------## 


 
#def recursive factorial algorithm
##


##------------------------------------------------## 

def rec_fact(x):
    """Returns x!

    Requires x>=0 and uses recursion"""

    print("\nIn rec_fact({})".format(x))


    #n0 value=0
    n0=0

    #base case
    if x==n0:
        print("It is now the base case.\n\nX currently is: {}".format(x)) 
        print("0!=1\n")
        return 1
    
    # x<>0 need to progress down to n0
    else:
        #current value
        print(f"X currently is: {x}\n")

        #reengage function with x-1
        next_valu=x*rec_fact(x-1)

        #way back up
        print(f"X currently is: {x}")
        print(f"{x}! is: {next_valu}\n")
        return next_valu

user_input=int(input("Please enter a non-negative number: "))

if user_input>=0:
    #nonneg
    answer=rec_fact(user_input)

    print("\nFinal Answer:\n{}! = {}".format(user_input,answer))

else:
    #neg
    print("Please enter a non-negative number.")