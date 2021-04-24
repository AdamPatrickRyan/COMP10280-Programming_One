##------------------Practical 4 HW2----------------##
## 
##User:     Aryan
##DC:       2020-10-01
##DLM:      2020-10-01
##MC:       COMP10280
##SD:       Currency Conversion
##
##------------------Practical 4 HW2----------------## 

##------------------Algorithm----------------------## 

##Algorithm is as follows

#Take entry amount

#Check if entry amount is float-able. 
##  If so convert to float and check if positive
###     If positive Accept, 
###     Else Reject.
##  Else return error.

#When input is float:
#Take amount conversion value (Conversion today for Euro to Dollar is 1.17427 according to X E). Note: I'm assuming we are not meant to take our student number as the currency conversion also since it asks us to use todays exchange rate
#Multiply input by conversion = Converted Value
#Print answer

##------------------------------------------------## 


def text_to_float(user_inp_value):
    "This function converts an input to a float or returns error"
    try:
        #Can be converted to float
        fl_entry=float(user_inp_value)

        if fl_entry >= 0:
            #Positive - return flag that it's valid and amount
            return [1,fl_entry]
        
        else:
            #Negative
            print('You entered a negative value to convert. Please enter an amount greater or equal to zero. You entered: {}'.format(user_inp_value))
            return [0, 0]

    except:
        #Can't be be converted to float
        print('You entered {} which is not a number; please choose another number'.format(user_inp_value))            
        return [0,0]

def static_currency_converter(input_amount, exchange_rate):
    "This multiplies inputs and returns a print statement and the amount"
    converted_value=input_amount*exchange_rate
    orig_currency_name='Euro'
    new_currency_name='US Dollars'
    print_statement="{} amount is: {}\nExchange rate to {} is: {}\n{} amount is: {}".format(orig_currency_name,input_amount,new_currency_name,euro_to_usd,new_currency_name,converted_value)

    return [converted_value, print_statement]

def job(user_inp_value,exchange_rate):
    "This runs the job"

    amount_to_convert_list=text_to_float(user_inp_value)


    success_check_input=amount_to_convert_list[0]
    amount_to_convert=amount_to_convert_list[1]

    if success_check_input==1:
        #Converted Successfully
        conversion_list=static_currency_converter(amount_to_convert,exchange_rate)
        conversion_amount=conversion_list[0]
        print_statement=conversion_list[1]
        print(print_statement)

        return
    else:
        #Unsuccessful - negative or letters

        return



user_input=input('Please enter a positive euro amount to convert into US Dollars: ')
euro_to_usd=1.17427

job(user_input,euro_to_usd)
