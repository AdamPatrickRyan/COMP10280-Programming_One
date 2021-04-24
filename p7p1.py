##------------------Practical 7 HW4----------------##
## 
##User:     Aryan
##DC:       2020-10-08
##DLM:      2020-10-08
##MC:       COMP10280
##SD:       Leap Check
##
##------------------Practical 7 HW4----------------## 

##------------------Algorithm----------------------## 

#L7 Slide 20
#Prompt the user for a year
# Read the year
# 
# if year>=0
#   if(year mod 4 = 0 and year mod 100 != 0) or year mod 400 = 0
#       Print(“Year is a leap year”)
#   else
#   Print(“Year is not a leap year”)
# else
#   Tell the user that the year must be positive
# 
# 
# Program finishes

##------------------------------------------------## 

#Static values
input_value=input('Please enter a year: ')
leap_statement='{} is a leap year'
notleap_statement='{} is not a leap year'
positive_statement='The year you enter must be positive'

year=int(input_value)

if year>=0:
    if (year%4==0 and year%100!=0) or (year%400==0):
        print(leap_statement.format(year))
    else:
        print(notleap_statement.format(year))

else:
    print(positive_statement)
