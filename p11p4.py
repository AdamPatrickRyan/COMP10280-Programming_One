##------------------Practical P11Q3----------------##
## 
##User:     Aryan
##DC:       2020-10-15
##DLM:      2020-10-15
##MC:       COMP10280
##SD:       Practical - Catalan
##
##------------------Practical P11Q3----------------## 


##------------------Algorithm----------------------## 


#a_0,

#while input positive
#if one print append the first number to string and end
#Otherwise calculate next and repeat.


##------------------------------------------------## 


#Static
user_input_number = int(input('Enter the number of terms you want the Catalan Sequence up to: '))
f_0=1

#It says terminate when negative but the 0th term doens't make sense so I'm terminating for non-positive
if user_input_number>0:
    series_string="The Catalan Sequence up to {} terms is: ".format(user_input_number)

    if user_input_number==1: #already defined
        series_string+="{}".format(f_0)

    else: #>1
        series_string+='{}'.format(f_0)
        a=f_0

        for count in range(1,user_input_number):
            n=count-1
            b=int(((2*((2*n) + 1))/(n+2))*(a))
            series_string+=", {}".format(b) #append to series
            a=b #swap

    print(series_string)
    #user_input_number = int(input('Enter another number of terms you want the Catalan Sequence up to: ')) - not asked in question

else: #nonpositive 
    print('You entered a non-positive number')


#msame as previous part but with for instead