##------------------Practical P11Q3----------------##
## 
##User:     Aryan
##DC:       2020-10-15
##DLM:      2020-10-15
##MC:       COMP10280
##SD:       Practical - Fibonnaci
##
##------------------Practical P11Q3----------------## 


##------------------Algorithm----------------------## 


#a_0, a_1, a_1+a_2=a_3, ...

#while input positive
#if one print append the first number to string and end
#Otherwise append first two to string, and for the counter up to input get third value, append to string, swap values and continue.


##------------------------------------------------## 


#Static
user_input_number = int(input('Enter the number of terms you want the Fibonacci Sequence up to: '))
f_0,f_1=0,1

#It says terminate when negative but the 0th term doens't make sense so I'm terminating for non-positive
while user_input_number>0:
    series_string="The Fibonnaci Series up to {} terms is: ".format(user_input_number)

    if user_input_number==1: #already defined
        series_string+="{}".format(f_0)

    else: #>1
        series_string+='{}, {}'.format(f_0,f_1)
        a,b=f_0,f_1

        for count in range(2,user_input_number):
            c=a+b
            series_string+=", {}".format(c) #append to series
            a,b=b,c #swap

    print(series_string)
    user_input_number = int(input('Enter another number of terms you want the Fibonacci Sequence up to: '))

else: #nonpositive 
    print('You entered a non-positive number')


#msame as previous part but with for instead