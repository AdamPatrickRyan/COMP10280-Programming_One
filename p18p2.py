##------------------Practical P18Q2----------------##
## 
##User:     Aryan
##DC:       2020-10-29
##DLM:      2020-10-29
##MC:       COMP10280
##SD:       Practical - Code count
##
##------------------Practical P18Q2----------------## 


##------------------Algorithm----------------------## 

#Input, Count code, return done.

##------------------------------------------------## 


def code_check(s):
    """Checks whether the string contains code."""

    count=s.count('code')

    return count

user_input = input("Enter a string to count 'code':  ")
code_count=code_check(user_input)

if code_count==1:
    x='.'
else:
    x='s.'

print(f"In your string 'code' appears: {code_check(user_input)} time{x}")

#code_check is the function asked for.