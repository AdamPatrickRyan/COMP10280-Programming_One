##------------------Practical P8Q1----------------##
## 
##User:     Aryan
##DC:       2020-10-15
##DLM:      2020-10-15
##MC:       COMP10280
##SD:       Practical - divisibility check
##
##------------------Practical P8Q1----------------## 


##------------------Algorithm----------------------## 

#Take Entry as number
#Convert to int
#Set up a counter for each mod

#If int >=0 then run (0=0 for all)
    #For int, check if mod counter is 0. If 0, print
    #Once finished request again
#   If value >0 than divved by number
#Else int<0, print statement.

##------------------------------------------------## 

#Static values

user_input=input('Please enter a non-negative integer: ')

limit=int(user_input)

mod_chk_1=2
mod_chk_2=3
mod_chk_3=5
mod_chk_4=7

print_statement="The number {} is divisible by: {}"

#Negative check
while limit>=0:


    #Need to reset result in each loop
    mod_r_1=0
    mod_r_2=0
    mod_r_3=0
    mod_r_4=0

    #check results
    mod_r_1=limit%mod_chk_1
    mod_r_2=limit%mod_chk_2
    mod_r_3=limit%mod_chk_3
    mod_r_4=limit%mod_chk_4

    if mod_r_1==0 or mod_r_2==0 or mod_r_3==0 or mod_r_4==0:
        print('{} is divisible by the following numbers: '.format(limit))

        if mod_r_1==0:
            print(mod_chk_1)

        if mod_r_2==0:
            print(mod_chk_2)


        if mod_r_3==0:
            print(mod_chk_3)

        if mod_r_4==0:
            print(mod_chk_4)
        
    else:
        print('The number is not divisible by {}, {}, {}, {}'.format(mod_chk_1,mod_chk_2,mod_chk_3,mod_chk_4))

 
    user_input=input('Please enter a non-negative integer: ')
    limit=int(user_input)

else:
    print('Number entered should be >= 0.')

#Better way: Make list of answers, for x in list of answers if x is 0 append to print list, print print list.