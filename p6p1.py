##------------------Practical 6 HW4----------------##
## 
##User:     Aryan
##DC:       2020-10-08
##DLM:      2020-10-08
##MC:       COMP10280
##SD:       Sum total 100 check
##
##------------------Practical 6 HW4----------------## 

##------------------Algorithm----------------------## 

#if no error:
#Get input 1 and 2 - don't validate with try/catch for input as not asked
#Check the sum
#print if >100

#error: 
#conversion error so print message


##------------------------------------------------## 

#Static values
check_value=100
output_print_statement='That is a big number!'
input_print_statement="Please enter the {} integer: " #position is a variable

#Begin
input_value_a=input(input_print_statement.format('first'))
input_value_b=input(input_print_statement.format('second'))

int_a=int(input_value_a)
int_b=int(input_value_b)

sum_total=int_a+int_b

#Strictly greater check
if sum_total>check_value:
    print(output_print_statement)

#Nothing else needed so end.