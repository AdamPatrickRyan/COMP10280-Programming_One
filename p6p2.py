##------------------Practical 6 HW4----------------##
## 
##User:     Aryan
##DC:       2020-10-08
##DLM:      2020-10-08
##MC:       COMP10280
##SD:       Odd max check - did two ways, second is neater but I thought of it later
##
##------------------Practical 6 HW4----------------## 

##------------------Algorithm----------------------## 

#if no error:
#Get input 1 and 2 and 3 - don't validate with try/catch for input as not asked
#Check parity of numbers

#If a is odd:

    ##Check if b is odd:

        ###Check if c is odd:

        ####All three are odd so get the largest using if else

        ###If c is not odd then check if a or b are larger

    ##If b is not odd:

        ###Check if c is odd

            ####a and c are odd check the largest

        ###If c is not odd: 

            ####a is the largest

#if a is not odd

    ##check if b is odd:

        ###check if c is odd:

            ####b and c are odd so get the largest

        ###if c is not odd:
            ####b is the largest

    ##if b is not odd

        ###check if c is odd:
            ####c is the largest

        ###if c is not odd then none are odd
    
######ALTERNATIVE#####
#A nicer way is probably to order them from a1, a2, a3 where a1>=a2>=a3 and then check if a1 odd, a2 odd, a3 odd and then you already have order


#I'm assuming we can't use loops etc.


##------------------------------------------------## 

#Static values
output_error_print_statement='You did not enter an odd number'
input_print_statement="Please enter your {} chosen integer: " #position is a variable

#Begin
input_value_a=input(input_print_statement.format('first'))
input_value_b=input(input_print_statement.format('second'))
input_value_c=input(input_print_statement.format('third'))

#Int conversion
int_a=int(input_value_a)
int_b=int(input_value_b)
int_c=int(input_value_c)

parity_a=int_a%2
parity_b=int_b%2
parity_c=int_c%2

odd_max=None

#not sure if we can use max function which would make this neater so avoiding

#check if any are odd to avoid wasting time if not
if parity_a==1 or parity_b==1 or parity_c==1: 

    if parity_a==1:
        #a is odd

        if parity_b==1:
            #b is odd

            if parity_c==1:
                #c is odd

                if int_a>=int_b and int_a>=int_c:
                    #all three are odd and max is a as a>b, a>c
                    odd_max=int_a
                
                elif int_b>=int_a and int_b>=int_c:
                    #all three are odd and b>=c, b>=a
                    odd_max=int_b

                else:
                    #all three are odd and 1 implies either a<b or a<c, 2 implies b<a or b<c, so for both to fail c>a and c>b 
                    odd_max=int_c

            else:
                #c is not odd, but a and b are

                if int_a>=int_b:
                    #a >= b
                    odd_max=int_a

                else:
                    #b>a
                    odd_max=int_b
            
        else:
            #b is not odd but a is

            if parity_c==1:
                #c and a are odd

                if int_a>=int_c:
                    #a >= c
                    odd_max=int_a

                else:
                    #c>a
                    odd_max=int_c
            
            else:
                #a is odd, b is not, c is not
                odd_max=int_a
    
    else:
        #a is not odd

        if parity_b==1:
            #b is odd

            if parity_c==1:
                #c is odd

                if int_b>=int_c:
                    #b and c are odd - b>=c
                    odd_max=int_b
            

                else:
                    #c>b and both odd 
                    odd_max=int_c

            else:
                #c is not odd, but b is

                odd_max=int_b


        else:
            #a and b are not odd, we've already checked for c in the parity check of a, b or c
            odd_max=int_c

else:
    #none odd
    print(output_error_print_statement)

if odd_max!=None:
    #odd max number assigned
    print("Out of {}, {}, and {}, the largest odd number is: {}".format(int_a,int_b,int_c,odd_max))


#alt - this way is much neater - code not fully tested below but is a better way of doing the above

##Get max first
#if int_a>=int_b and int_a>=int_c:
    #a max
#    max_num=int_a
#elif int_b>=int_a and int_b>=int_c:
#    #b max
#    max_num=int_b
#else:
#    max_num=int_c

##get second highest next
#if int_a<=int_b<=int_c:
#    second_max_num=int_b
#elif int_b<=int_a<=int_c:
#    second_max_num=int_a
#else:
#    second_max_num=int_c

#get third highest
#if int_a<=int_b and int_a<=int_c:
    #a least
#    third_max_num=int_a
#elif int_b<=int_a and int_b<=int_c:
    #b least
#    third_max_num=int_b
#else:
#    third_max_num=int_c
#
#
#if max_num%1==1:
#    odd_max=max_num
#
#else:
#    if second_max_num%1==1:
#        odd_max=second_max_num
#
#    else:
#        if third_max_num%1==1:
#            odd_max=third_max_num
#        else:
#            print(output_error_print_statement)
