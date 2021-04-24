##------------------Practical 7 HW4----------------##
## 
##User:     Aryan
##DC:       2020-10-08
##DLM:      2020-10-08
##MC:       COMP10280
##SD:       number and square
##
##------------------Practical 7 HW4----------------## 

##------------------Algorithm----------------------## 

#Take N\{0} as the set
#While counter is less than limit print counter and count^2


##------------------------------------------------## 

#Static values
counter=1
limit=50
counter_statement="The number is {} and its square is {}."

while counter<=limit:
    square_counter=counter**2
    print(counter_statement.format(counter,square_counter))
    counter+=1