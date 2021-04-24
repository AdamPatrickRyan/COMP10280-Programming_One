##------------------Practical P10Q3----------------##
## 
##User:     Aryan
##DC:       2020-10-15
##DLM:      2020-10-15
##MC:       COMP10280
##SD:       Practical - Letter count
##
##------------------Practical P10Q3----------------## 


##------------------Algorithm----------------------## 


#Check if not empty, strip case, Loop through letters, check for vowels, count for vowel




##------------------------------------------------## 

import sys

#Static values
chk1='a'
chk2='e'
chk3='i'
chk4='o'
chk5='u'

print_statement="The vowel count in the string is: \n{}: \t {}\n{}: \t {}\n{}: \t {}\n{}: \t {}\n{}: \t {}"

user_input=input("Please enter something not empty to count the vowels: ")



while user_input!='':
    lower_user_input=user_input.lower() #strip to lower to remove case sensitive
    chk1_count=0
    chk2_count=0
    chk3_count=0
    chk4_count=0
    chk5_count=0

    for letter in lower_user_input:
        if letter==chk1:
            chk1_count+=1

        elif letter==chk2:
            chk2_count+=1
        
        elif letter==chk3:
            chk3_count+=1

        elif letter==chk4:
            chk4_count+=1

        elif letter==chk5:
            chk5_count+=1

    print(print_statement.format(chk1,chk1_count,chk2,chk2_count,chk3,chk3_count,chk4,chk4_count,chk5,chk5_count))

    user_input=input("Please enter something else not empty to count the vowels: ")


else:
    print("You terminated the program")