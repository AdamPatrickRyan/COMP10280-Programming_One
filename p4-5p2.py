##------------------Practical 4.5 HW3----------------##
## 
##User:     Aryan
##DC:       2020-10-06
##DLM:      2020-10-06
##MC:       COMP10280
##SD:       Geometric Shapes
##
##------------------Practical 4.5 HW3----------------## 

##------------------Algorithm----------------------## 

##Formulas:
#square area = Length^2
#Cube volume = Length^3
#circle are = 2pir
#Volume Sphere = (4/3) pi r^3 = (4/3)*pi*(D/2)^3
#Volume of cylinder = pi r^2 h

#Take input and chexk valid (lengths and diameters are positive)
#Run functions for appropriate item.



##------------------------------------------------## 


#Module import

import math as mt

input_value=input("Please enter a length: ")

#Not checking if valid entry per Brightspace comment
float_user_input=float(input_value)

if float_user_input>=0:
    side_length=float_user_input
    diameter=float_user_input

    pi_value=mt.pi
    #   "This function calculates the area of a square"
    sq_area=side_length**2
    print('The area of a square with a side length of {} is: \n{}\n'.format(side_length,sq_area))


    cu_volume=side_length**3
    print('The volume of a cube with a side length of {} is: \n{}\n'.format(side_length,cu_volume))
    

    #   "This function calculates area of a circle"
    ci_area=pi_value*diameter
    print('The area of a circle with a diameter of {} is: \n{}\n'.format(diameter,ci_area))


    #    "This function calculates volume of a sphere"
    sp_volume=(4/3)*pi_value*(diameter/2)**3
    print('The volume of a sphere with a diameter of {} is: \n{}\n'.format(diameter,sp_volume))



    #    "This function calculates volume of a cylinder"
    cy_volume=pi_value*((diameter/2)**2)*(diameter)
    print('The volume of a cylinder with a diameter of {} and a height of {} is: \n{}\n'.format(diameter,diameter,cy_volume))

else:
    print_statement='Length must be >= 0. Please try again'
    print(print_statement)