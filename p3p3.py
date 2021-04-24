##------------------Practical 3 HW2----------------##
## 
##User:     Aryan
##DC:       2020-10-01
##DLM:      2020-10-01
##MC:       COMP10280
##SD:       Geometric Shapes
##
##------------------Practical 3 HW2----------------## 

##------------------Algorithm----------------------## 

#Get inputs (upper proportion, upper rate, total, lower prop, lower rate)
#Convert rates and proportions to figures between 0 and 1
#Get total amount at each rate
#Get tax amount due for each band
#Add relevant amounts

##------------------------------------------------## 



taxable_amount=143950.76

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


#Calculate tax for upper amount
amount_at_upper_rate=taxable_amount*upper_prop_percent
tax_at_upper_rate=amount_at_upper_rate*upper_rate_percent

#Calculate tax for lower amount
amount_at_lower_rate=taxable_amount*lower_prop_percent
tax_at_lower_rate=amount_at_lower_rate*lower_rate_percent

#Tax and total due
tax_due=tax_at_lower_rate+tax_at_upper_rate
total_due=tax_due+taxable_amount

print(f"""
The initial amount is: {taxable_amount} \n
The tax on the larger amount is: {tax_at_upper_rate} \n
The tax on the smaller amount is: {tax_at_lower_rate} \n
The tax due is {tax_due} \n
The total amount due is {total_due} \n
""")