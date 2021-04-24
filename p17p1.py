##------------------Practical P17Q1----------------##
## 
##User:     Aryan
##DC:       2020-10-27
##DLM:      2020-10-27
##MC:       COMP10280
##SD:       Practical - Divisors
##
##------------------Practical P17Q1----------------## 


##------------------Algorithm----------------------## 

#Code from lecture 16 P14 modified

#Inputs
#if both >0:
# find divisors.
# add to print statement
# strip brackets from statement.


##------------------------------------------------## 



def findDivisors(num1):
    f"""Finds the common divisors of num1 and num2
     
    Assumes that num1 and num2 are positive integers - Returns a tuple containing the common divisors of num1 and num2"""

    divisors = (1,num1)

    for i in range(2, (num1//2) + 1):
        #1 is a divisor, no numbers after floor(x/2)+1 can be a divisor as 1<num/floor(x/2)+1<2 -> Non int
        if num1 % i == 0:
            divisors += (i,)

    return divisors



#Static
#it works by making an empty tupled, getting min of entry 1 and 2 (as max(div(x,y)<=min(x,y)), and adding any divisors to the tuple.
user_entry_1=int(input('Please enter a positive integer: '))
print_statement="The divisors of {} and are: ".format(user_entry_1)

#add all characters to remove from the final string - we don't want () in the list of divisors as it doesn't look neat
print_strip_config_1="(" 
print_strip_config_2=")"
#Technically it's better to use re.sub and list but we'e not done this in lectuers so not sure if allowed? would neaten the .replace().replace()

if user_entry_1<=0:
    print_statement="The number must be positive"
else:
    div_tuple=findDivisors(user_entry_1)
    print_statement+="{}".format(div_tuple)
    print_statement=print_statement.replace(print_strip_config_1,"",-1).replace(print_strip_config_2,"",-1)
        
print(print_statement)
    
    