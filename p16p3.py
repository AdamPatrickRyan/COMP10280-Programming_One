##------------------Practical P16Q1----------------##
## 
##User:     Aryan
##DC:       2020-10-27
##DLM:      2020-10-27
##MC:       COMP10280
##SD:       Practical - Perfect n
##
##------------------Practical P16Q1----------------## 


##------------------Algorithm----------------------## 

#Even perfect numbers are of the form 2^{p-1} (M(p)) where M(p) is Mersenne prime with power p -> see MATH10040.

#One method (presume not desired?):
#Get an upper bound on M(p) via input (p <= floor(log_2(input +1)))
#Check primes to p
#Lucas Lehmer to check Mersenne primes
#produce list
#odd - lower bound on an odd perfect number is 10^160: https://www.jstor.org/stable/2008375?seq=1 
#if number is less than this done. Else implement slow algorithm
  
#alt:
##Function 1: Get the divisors and sum of the divisors <- I thought we would need to print divisors based on it saying in Q 6=3+..+1
##Function 2: Check if sum of divisors is number
##Function 3: Encapsulate the above and return a number if its perfect

#While entry>=1:
#for number in 1 to entry:
##get divisiors anf sum of number
##check if number is perfect
##add number to list if perfect.
#print statement


##------------------------------------------------## 


#Functions

def findDivisorsPlusSum(num1):
    f"""Finds the  divisors of num1
     
    Assumes that num1 integers
    Returns a tuple containing the divisors of num1, and the sum total"""

    print(f"\nIn findDivisors for {num1}:")

    #Default
    divisors = (1,)

    sum_total=1

    if num1==1:
        output_list=[divisors,sum_total]
        return output_list
    else:  
        for i in range(2, (num1//2)+1):
            #check up to lower floor(x/2)+1 as anything else obviously can't be a divisor except num1
            if num1 % i == 0:
                divisors += (i,)
                sum_total+=i #excludes number since that would obviously not be good

        output_list=[divisors,sum_total]

        return output_list

def checkPerfect(number,sum_of_div):
    """Checks if the sum of divisors is perfect"""

    print(f'\nIn checkPerfect for {number}:')
    output=False

    #if true it's perfect.
    if number==sum_of_div:
        output=True
    
    print(f"Is {number} perfect? {output}")
    return output

def number_perfect(number):
    f"""Given a number returns the number if it's perfect
    
    Ensapulation of findDivisors and checkPerfect"""

    print(f"\n\nIn number_perfect for {number}:")

    #List of divisors and sum
    div_sum_list=findDivisorsPlusSum(number)
    div_sum=div_sum_list[1]

    #check if perfect
    num_is_perfect=checkPerfect(number,div_sum)

    if num_is_perfect==True:
        print(f"A perfect number was found: {number}\nThe set of divisors are: {div_sum_list[0]}")
        return number
    else:
        return

#Note: Split as functions above for versatility of:
#-Getting divisors and sum of divisors
#-Checking if perfect
#-Audit
#This could technically be done in the first function just by returning number if sum_total=num1

#Static
user_entry_1=int(input('Please enter a positive integer: '))
perfectnumlist=[]

while user_entry_1>=1:
    print_statement=f"\n\nThe perfect numbers up to {user_entry_1} are: "
    perfectnumlist=[]

    for x in range(1,user_entry_1+1):
        print("\n\n----")
        if number_perfect(x)==x:
            #The number is perfect
            perfectnumlist.append(x)

    print("\n\n----")
    print_statement+="{}".format(perfectnumlist)
    print_statement=print_statement.replace("[","",-1).replace("]","",-1)
    print(print_statement)

    user_entry_1=int(input('\nPlease enter another positive integer: '))

else:
    print('That is non-positive, the program has been terminated.')





