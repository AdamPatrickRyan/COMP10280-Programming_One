##------------------Practical 4 HW2----------------##
## 
##User:     Aryan
##DC:       2020-10-01
##DLM:      2020-10-01
##MC:       COMP10280
##SD:       Tax
##
##------------------Practical 4 HW2----------------## 

##------------------Algorithm----------------------## 

##Formulas:
#Get input and checks valid
#Split into upper and lower tax bracket
#Find tax amount for each bracket
#Add amounts.

##------------------------------------------------## 

#Note: This function is almost identical to what I wrote in P4P1, as this is almost in each question in sheet 4 - difference is in print statement
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
            print('Please enter a positive value; negative tax amounts are not valid. You entered: {}'.format(user_inp_value))
            return [0, 0]

    except:
        #Can't be be converted to float
        print('You entered {} which is not a number; please choose a number'.format(user_inp_value))            
        return [0,0]

def tax_upper_bracket(percent_at_upper_rate,taxable_amount,upper_tax_rate):
    "Calculate amount of tax due at upper rate"
    amount_at_upper_rate=percent_at_upper_rate*taxable_amount
    tax_due_at_upper_rate=amount_at_upper_rate*upper_tax_rate
    return tax_due_at_upper_rate


def tax_lower_bracket(percent_at_lower_rate,taxable_amount,lower_tax_rate):
    "Calculate amount of tax due at lower rate" #technically not necessary in this case as identical to upper
    
    amount_at_lower_rate=percent_at_lower_rate*taxable_amount
    tax_due_at_lower_rate=amount_at_lower_rate*lower_tax_rate
    
    return tax_due_at_lower_rate

def total_amount_due(taxable_amount,percent_at_upper_rate,upper_tax_rate,percent_at_lower_rate,lower_tax_rate):
    "Returns tax upper, tax lower, total tax, total due"
    tax_upper=tax_upper_bracket(percent_at_upper_rate,taxable_amount,upper_tax_rate)
    tax_lower=tax_lower_bracket(percent_at_lower_rate,taxable_amount,lower_tax_rate)

    total_due= tax_upper+tax_lower+taxable_amount

    total_tax=tax_lower+tax_upper

    output_list=[tax_upper, tax_lower, total_tax, total_due]

    return output_list

def job():
    "Run job"
    input_taxable_amount=input("Please enter a positive taxable amount: ")

    taxable_amount_list=text_to_float(input_taxable_amount)

    success_check=taxable_amount_list[0]
    taxable_amount=taxable_amount_list[1]

    if success_check==1:
        #Converted successfully to float

        #Upper refers to larger amount of total
        upper_prop=60
        upper_rate=13.5
        upper_prop_percent=upper_prop/100.0
        upper_rate_percent=upper_rate/100.0

        #Lower refers to lower amount of total
        lower_prop=40
        lower_rate=23
        lower_prop_percent=lower_prop/100.0
        lower_rate_percent=lower_rate/100.0

        tax_list=total_amount_due(taxable_amount, upper_prop_percent, upper_rate_percent, lower_prop_percent, lower_rate_percent)
        
        #Taxes
        tax_at_upper_rate=tax_list[0]
        tax_at_lower_rate=tax_list[1]
        tax_due=tax_list[2]

        #Total
        total_due=tax_list[3]

        print(f"""
The initial amount is: {taxable_amount} \n
The tax on the larger amount is: {tax_at_upper_rate} \n
The tax on the smaller amount is: {tax_at_lower_rate} \n
The tax due is: {tax_due} \n
The total amount due is: {total_due} \n
        """)

        return

    else:
        #Negative or non-number
        return

job()