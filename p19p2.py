##------------------Practical P19Q2----------------##
## 
##User:     Aryan
##DC:       2020-10-29
##DLM:      2020-10-29
##MC:       COMP10280
##SD:       Practical - Base converter
##
##------------------Practical P19Q2----------------## 


##------------------Algorithm----------------------## 


#Similar to p19p1.

#a=sum_{i=0}^{i=n-1} a_i * b^(i) = pq+r where n=number of digits
#check valid digits
#formula above

##------------------------------------------------## 

def base_convertion(input_string, input_base):
    
    digits=len(input_string)
    sum_st=0

    dig_string=[x for x in input_string.lower()]
    dig_string.reverse()
    allowed_chars='0123456789abcdef'
    
    validator=True

    for x in dig_string:
        if x not in allowed_chars:
            validator='False'
        
    if validator:

        for i in range(0,digits):
            base_power=input_base**i
            term=dig_string[i]

            if term=='a':
                digit=10
            elif term=='b':
                digit=11
            elif term=='c':
                digit==12
            elif term=='d':
                digit==13
            elif term=='e':
                digit=14
            elif term=='f':
                digit=15
            else:
                digit=int(term)
            
            sum_st+=base_power*digit

        print("In base 10, your number is",sum_st)


    else:
        print('You entered an invalid character in your string.')
    return sum_st


user_input=input('Enter a positive integer to convert to base 10: ')
user_base=int(input('Enter a positive integer to representing the base: '))
base_convertion(user_input,user_base)







