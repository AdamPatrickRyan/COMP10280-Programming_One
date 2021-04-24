##------------------Practical P10Q1----------------##
## 
##User:     Aryan
##DC:       2020-10-15
##DLM:      2020-10-15
##MC:       COMP10280
##SD:       Practical - CubeRoot
##
##------------------Practical P10Q1----------------## 


##------------------Algorithm----------------------## 


#Check if =0, if yes end

#If it's negative convert to positive as one of the roots in Z

#loop up to number, check if cube is equal abs entered number. 

#if yes flag root found. If no and loop is over then print not a perfect cube.

#Ask for input again




##------------------------------------------------## 

import sys

#Static values
int_user_input=int(input("Please enter a non-zero number to find its integer cube root, or 0 to exit: "))

while int_user_input!=0:
    cube_found=0

    #Convert to positive
    if int_user_input<0:
        pos_user_input=int_user_input*(-1)

    else:
        pos_user_input=int_user_input

    #Loop
    for k in range(pos_user_input+1):
        k_cu=k**3

        if k_cu==pos_user_input:
            cube_found=1
            #Alternative is break
            print("{} is a perfect cube, with an integer root of {}.".format(int_user_input,k))
        
    #Loop over
    if cube_found==0:
        print("{} is not a perfect cube.".format(int_user_input))

    #Request again
    int_user_input=int(input("Please enter a non-zero number to find its integer cube root, or 0 to exit: "))


else:
    print('You entered 0.')