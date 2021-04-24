##------------------Practical 4 HW2----------------##
## 
##User:     Aryan
##DC:       2020-10-01
##DLM:      2020-10-01
##MC:       COMP10280
##SD:       Geometric Shapes
##
##------------------Practical 4 HW2----------------## 

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


#Define Functions

#Note: This function is almost identical to what I wrote in P4P1, as this is almost in each question in sheet 4 - difference is in print statement
def text_to_float(user_inp_value):
    "This function converts an input to a float or returns error"
    try:
        #Can be converted to float
        fl_entry=float(user_inp_value)

        if fl_entry >= 0:
            #Positive - return flag that it's valid and amount
            return [1,fl_entry]
        
        else:
            #Negative
            print('Please enter a positive value; negative lengths and diameters are not valid. You entered: {}'.format(user_inp_value))
            return [0, 0]

    except:
        #Can't be be converted to float
        print('You entered {} which is not a number; please choose a number'.format(user_inp_value))            
        return [0,0]


#Functions for areas
def area_square(side_length):
    "This function calculates the area of a square"
    area=side_length**2
    print('The area of a square with a side length of {} is: \n{}\n'.format(side_length,area))

def volume_cube(side_length):
    "This functions calculates the volume of a cube"
    volume=side_length**3
    print('The volume of a cube with a side length of {} is: \n{}\n'.format(side_length,volume))
 

def area_circle(diameter,pi_value):
    "This function calculates area of a circle"
    area=pi_value*diameter
    print('The area of a circle with a diameter of {} is: \n{}\n'.format(diameter,area))


def volume_sphere(diameter,pi_value):
    "This function calculates volume of a sphere"
    volume=(4/3)*pi_value*(diameter/2)**3
    print('The volume of a sphere with a diameter of {} is: \n{}\n'.format(diameter,volume))


def volume_cylinder(diameter,pi_value):
    "This function calculates volume of a cylinder"
    volume=pi_value*((diameter/2)**2)*(diameter)
    print('The volume of a cylinder with a diameter of {} and a height of {} is: \n{}\n'.format(diameter,diameter,volume))

#Note: Functions above are the same as those I wrote in P3P2 as it's an identical request

def job(length,pi_value):
    print("The length you entered is: {length}")
    area_square(length)
    volume_cube(length)
    area_circle(length,pi_value)
    volume_sphere(length,pi_value)
    volume_cylinder(length,pi_value)

def run_job():
    input_value=input("Please enter a length: ")
    pi_value=mt.pi
    converted_input_list=text_to_float(input_value)

    success_check=converted_input_list[0]
    converted_value=converted_input_list[1]

    if success_check==1:
        job(converted_value,pi_value)
        return
    else:
        return

run_job()