##------------------Practical P8Q2----------------##
## 
##User:     Aryan
##DC:       2020-10-15
##DLM:      2020-10-15
##MC:       COMP10280
##SD:       Practical - divisibility check
##
##------------------Practical P8Q2----------------## 


##------------------Algorithm----------------------## 

#Take Entry as number
#Convert to int
#Set up a counter for each mod

#If int >0 then run (0=0)
# For each column <=number:
#   For each row, go through all of the values up to the limit multiplied by the number and add to a string which you print
#Reset the string, reset the bit that goes through each number up to limit for columns, and add one to get to the next column.
#Repeat until both are >number


##------------------------------------------------## 

#Static values

user_input=input('Please enter a non-negative integer: ')

limit=int(user_input)
x_axis=1
y_axis=1

if limit==0:
    print("The multiplication table for 0 is: \n 0")

elif limit<0:
    print('Please enter a non-negative int')

#Multiplication Table
else:
    print("\nThe multiplication table for", limit, "is: \n")
    
    #y-value
    while y_axis<=limit:

        #Set the row as blank in each loop
        print_string=''

    #x_value
        while x_axis<=limit:

            #Result of multi
            multivalue=x_axis*y_axis

            #Add to string
            print_string+='{} '.format(multivalue) #Technically length of multivalue will throw out but don't know good way to fix
            x_axis+=1
        
        #Not sure how to justify nicely?
        print(print_string)

        #Go down to next row
        y_axis+=1

        #reset value for going across the table
        x_axis=1

#Done


