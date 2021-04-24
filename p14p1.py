##------------------Practical P13Q5----------------##
## 
##User:     Aryan
##DC:       2020-10-20
##DLM:      2020-10-20
##MC:       COMP10280
##SD:       Practical - Factorial Time Analysis

##------------------Practical P13Q5----------------## 


##------------------Algorithm----------------------## 


 
#def recursive factorial algorithm
#def non_recursive factorial algo
#import clock time to check time for each
#run for loop on 10*x and compare output time of both
##put in an except for recursion because it'll fail at max recursion depth.



##------------------------------------------------## 

import time

#from my answers previously
def rec_fact(x):
    """Returns x!

    Requires x>=0 and uses recursion"""

    #print("\nIn rec_fact({})".format(x))


    #n0 value=0
    n0=0

    #base case
    if x==n0:
        #print("It is now the base case.\n\nX currently is: {}".format(x)) 
        #print("0!=1\n")
        return 1
    
    # x<>0 need to progress down to n0
    else:
        #current value
        #print(f"X currently is: {x}\n")

        #reengage function with x-1
        next_valu=x*rec_fact(x-1)

        #way back up
        #print(f"X currently is: {x}")
        #print(f"{x}! is: {next_valu}\n")
        return next_valu


def fact(pos_int):
    """Returns x!
    
    Returns the factorial of x for x>=0 int"""

    fact=1

    #multiply fact count
    for i in range(1, pos_int + 1):
        fact*= i

    return fact

print("|x    |   F   |   RF|")
for factor_x in range(1,20):
    #time to run factorial
    x=factor_x*100
    fact_func_start=time.time()
    fact(x)
    fact_func_end=time.time()
    fact_elapsedtime=fact_func_end-fact_func_start

    #Time to run recursion
    try:
        rec_fact_start=time.time()
        rec_fact(x)
        rec_fact_end=time.time()
        rec_fact_elapsedtime=rec_fact_end-rec_fact_start
    
    except:
        print('RecursionError: Maximum Recursion Depth Exceeded')

    print("|{}   |  {}   |   {}|".format(x,fact_elapsedtime,rec_fact_elapsedtime))

