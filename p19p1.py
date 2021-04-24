##------------------Practical P19Q1----------------##
## 
##User:     Aryan
##DC:       2020-10-29
##DLM:      2020-10-29
##MC:       COMP10280
##SD:       Practical - Base converter
##
##------------------Practical P19Q1----------------## 


##------------------Algorithm----------------------## 


#a=sum_{i=0}^{i=n-1} a_i * b^(i) = pq+r where n=number of digits 
#implement Euclid's division algorithm 
    #n=bq+r
    #n-r=bq
    #q=n-r /b
    #repeat for q>0.


##------------------------------------------------## 

def base_convertion(input_number, target_base):
    """Converts to a base under 11"""
    co_list=[]

    quotient=input_number

    while quotient>0:
        remainder=quotient%target_base
        co_list.append(remainder)
        quotient=int((quotient-remainder)/target_base)

    print_statement="In base {}, {} is written as: ".format(target_base,input_number)

    co_list.reverse()

    for coeff in co_list:
        print_statement+="{}".format(coeff)

    print(print_statement)
    return co_list


user_input=int(input('Enter a positive integer to convert the base: '))
user_base=int(input('Enter a positive integer under 11 to convert to base: '))

if user_base<=10:
    base_convertion(user_input,user_base)
else:
    print('Sorry, this tool only supports up to base 10')
    #Doesn;t say what max base we should support to avoid a_{10}, a_{11},..a_{b-1} etc.







