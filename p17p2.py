##------------------Practical P17Q2----------------##
## 
##User:     Aryan
##DC:       2020-10-27
##DLM:      2020-10-27
##MC:       COMP10280
##SD:       Practical - Common Divisors
##
##------------------Practical P17Q2----------------## 


##------------------Algorithm----------------------## 

#Code from lecture 16 P14 modified

#Inputs
#if both >0:
# find divisors.
# add to print statement
# strip brackets from statement.


##------------------------------------------------## 



def findDivisors(num1, num2):
    f"""Finds the common divisors of num1 and num2
     
    Assumes that num1 and num2 are positive integers - Returns a tuple containing the common divisors of num1 and num2"""

    divisors = (1,)

    for i in range(2, (min(num1, num2)//2) + 1):
        #1 is a divisor, no numbers after floor(x/2)+1 can be a divisor as 1<num/floor(x/2)+1<2 -> Non int
        if num1 % i == 0 and num2 % i == 0:
            divisors += (i,)

    if num1%min(num1,num2)==num2%min(num1,num2)==0: 
        #min number itself could be a divisor of both so check
        divisors+=(min(num1,num2),)

    return divisors



#Static
#it works by making an empty tupled, getting min of entry 1 and 2 (as max(div(x,y)<=min(x,y)), and adding any divisors to the tuple.
user_entry_1=int(input('Please enter a positive integer: '))
user_entry_2=int(input('Please enter a second positive integer: '))
print_statement="The common divisors of {} and {} are: ".format(user_entry_1,user_entry_2)

#Technically it's better to use re.sub and list but we'e not done this in lectuers so not sure if allowed? would neaten the .replace().replace()

if user_entry_1<=0 or user_entry_2<=0:
    print_statement="Both numbers must be positive"
else:
    div_tuple=findDivisors(user_entry_1,user_entry_2)
    print_statement+="{}".format(div_tuple)
    print_statement=print_statement.replace("(","",-1).replace(")","",-1)
        
print(print_statement)
    
    