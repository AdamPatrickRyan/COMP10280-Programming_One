##------------------Practical 7 HW4----------------##
## 
##User:     Aryan
##DC:       2020-10-08
##DLM:      2020-10-08
##MC:       COMP10280
##SD:       Triangular number mod 3 or mod 5
##
##------------------Practical 7 HW4----------------## 

##------------------Algorithm----------------------## 

#Take N as the set
#Set a limit and running total
#for counter  to limit+1
#Check if div 3 or 5 and if so add counter to running total
#Done

##------------------------------------------------## 

#Static values

limit=10000
running_total=0
mod_chk_1=3
mod_chk_2=5
print_statement='The sum of the natural numbers divisible by {} or {} up to {} is {}'

#1 up to limit inclusive
for counter in range(limit+1):
    #print(counter)

    #pass check so add to total
    if counter%mod_chk_1==0 or counter%mod_chk_2==0:
        running_total+=counter

#for loop finished so print answer
print(print_statement.format(mod_chk_1,mod_chk_2,limit,running_total))