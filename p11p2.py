##------------------Practical P11Q2----------------##
## 
##User:     Aryan
##DC:       2020-10-15
##DLM:      2020-10-15
##MC:       COMP10280
##SD:       Practical - Fibonnaci
##
##------------------Practical P11Q2----------------## 


##------------------Algorithm----------------------## 


#a_0, a_1, a_1+a_2=a_3, ...

#if negative fail. 

#Otherwise
#if one print append the first number to string and end
#Otherwise append first two to string, and while the counter < input get third value, append to string, swap values and continue.


##------------------------------------------------## 


#Static
user_input_number = int(input('Enter the number of terms you want the Fibonacci Sequence up to: '))
f_0,f_1=0,1
count=2
series_string="The Fibonnaci Series is: "

if user_input_number<=0: #negative
    print('You entered a non-positive number')

else: #positive

    if user_input_number==1: #already defined
        series_string+="{}".format(f_0)

    else: #>1
        series_string+="{}, {}".format(f_0,f_1)
        a,b=f_0,f_1

        while count<user_input_number:
            c=a+b
            series_string+=", {}".format(c) #append to series
            a,b=b,c #swap
            count+=1 #count+1

    print(series_string)

#more condensed than usual as asked to make small 