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
#Algorithm (from Wikipedia)
# The following pseudocode determines whether a year is a leapyear or a common year in the Gregorian calendar:
# if (year is not exactly divisible by 4) then (it is a common year)
# elseif (year is not exactly divisible by 100) then (it is a leap year)
# elseif (year is not exactly divisible by 400) then (it is a common year)
# else (it is a leap year)

##------------------------------------------------## 

#Static values
input_value=input('Please enter a year: ')
leap_statement='{} is a leap year'
notleap_statement='{} is not a leap year'
positive_statement='The year you enter must be positive'

year=int(input_value)

if (year%4!=0): #not div 4
    print(notleap_statement.format(year))

elif (year%100!=0): #div 4 not 100
    print(leap_statement.format(year))

elif (year%400!=0): #div 4 not 400
    print(notleap_statement.format(year))

else: #leapyear
    print(leap_statement.format(year))

#Wikipedia has no check on postivity