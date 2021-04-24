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


def code_check(string_one, string_two):
    """Check if either string one or string two at end of other string"""

    #length of strings
    len_string_one=len(string_one)
    len_string_two=len(string_two)

    string_one=string_one.lower()
    string_two=string_two.lower()

    Result=False

    if len_string_one==0 or len_string_two==0:
        #either empty then auto true
        Result = True

    else:
        #neither empty so check
        if len_string_one>len_string_two:
            end_slice=string_one[(-1*len_string_two):]
            #print(end_slice)
            #print(string_two)

            if end_slice==string_two:
                Result=True

        else:
            end_slice=string_two[(-1*len_string_one):]
            #print(end_slice)
            #print(string_one)

            if end_slice==string_one:
                Result=True       
        
    return Result

def job():
    user_input_1 = input("Enter a string:  ")
    user_input_2 = input("Enter a second string:  ")

    code_count=code_check(user_input_1, user_input_2)

    print(f"Does one of your strings appear at the end of the other? {code_count}")

job()