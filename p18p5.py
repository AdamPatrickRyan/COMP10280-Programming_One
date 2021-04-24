##------------------Practical P18Q4----------------##
## 
##User:     Aryan
##DC:       2020-10-29
##DLM:      2020-10-29
##MC:       COMP10280
##SD:       Practical - Start End String
##
##------------------Practical P18Q4----------------## 


##------------------Algorithm----------------------## 

#check which is bigger
#chcck if the slice at the end of the string is equal to smaller string.
#if either are empty return true.

##------------------------------------------------## 


def code_check(string_one):
    """Checks string for xyz and .xyz and if xyz count > .xyz count true"""

    #length of strings
    check='xyz'
    do_not_allow='.'+check

    check_count=string_one.count(check)
    not_allow_count=string_one.count(do_not_allow)

    #Include-Exclusion principle: If each instance of xyz will be counted in 1, in the other only .xyz counter. (1)-(2) = instances of xyz without . preceding it, and if >0 it appears at least once.
    total_count=check_count-not_allow_count

    if total_count>0:
        Result=True
    else:
        Result=False
        
    return Result

def job():
    user_input_1 = input("Enter a string:  ")
    code_count=code_check(user_input_1)

    print(f"Is xyz in the string without a . preceding it? {code_count}")

job()