##------------------Practical 3 HW2----------------##
## 
##User:     Aryan
##DC:       2020-10-01
##DLM:      2020-10-01
##MC:       COMP10280
##SD:       Currency Conversion
##
##------------------Practical 3 HW2----------------## 

##------------------Algorithm----------------------## 

##Algorithm is as follows
#
#My student number is 14395076 (143950.76)

#Take entry amount

#Take amount conversion value (Conversion today for Euro to Dollar is 1.17427 according to XE.com). 
#Multiply input by conversion = Converted Value
#Print answer

##------------------------------------------------## 

student_number=143950.76
euro_to_usd=1.17427
converted_amount=student_number*euro_to_usd
print_statement="{} amount is: {}\nExchange rate to {} is: {}\n{} amount is: {}".format('Euro',student_number,'US Dollars',euro_to_usd,'US Dollars',converted_amount)
print(print_statement)