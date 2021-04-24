##------------------Practical 1 HW1----------------##
## 
##User:     Aryan
##DC:       2020-09-29
##DLM:      2020-09-29
##MC:       COMP10280
##SD:       Print personal details
##
##------------------Practical 1 HW1----------------## 

my_name='Adam Ryan'
my_address = '158 Block A, Smithfield Market, Dublin 7'
my_phone='0834240698'

##Third program statement.
def personal_detail_print(name, address, phone):
    ##Define the statement and substitute variables with input
    statement="""My name is: {}\n\nMy address is: {}\n\nMy Phone Number is: {}""".format(name,address,phone)

    #Return print is valid in python 3
    return print(statement)

##Alternative if separate print statements are needed; this also runs.
def basic_print(name,address,phone):
    ##Print everything on a new line with nothing else.
    print("My name is: " + name + '\n')
    print("My address is: " + address + '\n')
    print("My phone number is: " + phone)
    return

personal_detail_print(my_name, my_address, my_phone)