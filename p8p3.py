##------------------Practical P8Q3----------------##
## 
##User:     Aryan
##DC:       2020-10-15
##DLM:      2020-10-15
##MC:       COMP10280
##SD:       Practical - Simple multi table
##
##------------------Practical P8Q3----------------## 


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
y_axis=0

#Clunky table format print
print("\n----------------------")
print(f"Times {limit} Table")
print("----------------------")
    
#not checking positive or negative - makes sense to have a minus and 0 times table even if boring    

#y-value
while y_axis<=20:
    multi_value=limit*y_axis

    #Slightly changing print statement to align
    if len(str(y_axis))==1:
        print_statement='|{} |     |        {}'
    else:
        print_statement='|{}|     |        {}'
    
    print(print_statement.format(y_axis,multi_value))
    y_axis+=1

