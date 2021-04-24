##------------------Practical 4.5 HW3----------------##
## 
##User:     Aryan
##DC:       2020-10-06
##DLM:      2020-10-06
##MC:       COMP10280
##SD:       Currency Conversion
##
##------------------Practical 4.5 HW3----------------## 

##------------------Algorithm----------------------## 

##Algorithm is as follows

#Take entry amount

#When input is float:
#Take amount conversion value (Conversion today for Euro to Dollar is 1.18033 according to XE). 
#Multiply input by conversion = Converted Value
#Print answer

##------------------------------------------------## 

        

user_input=input('Please enter a positive euro amount to convert into US Dollars: ')
float_user_input=float(user_input)
euro_to_usd=1.18033

#No check on valid float per comment on brightspace.

if float_user_input >= 0:
    #Positive - return flag that it's valid and amount
    amount_to_convert=float_user_input
    converted_amount=amount_to_convert*euro_to_usd
    print_statement="{} amount is: {}\nExchange rate to {} is: {}\n{} amount is: {}".format('Euro',amount_to_convert,'US Dollars',euro_to_usd,'US Dollars',converted_amount)
    print(print_statement)

else:
    #Negative
    print('Amount must be >= 0. Please try again')