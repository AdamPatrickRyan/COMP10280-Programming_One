##------------------Practical 3 HW2----------------##
## 
##User:     Aryan
##DC:       2020-10-01
##DLM:      2020-10-01
##MC:       COMP10280
##SD:       Geometric Shapes
##
##------------------Practical 3 HW2----------------## 

##------------------Algorithm----------------------## 

##Formulas:
#square area = Length^2
#Cube volume = Length^3
#circle are = 2pir
#Volume Sphere = (4/3) pi r^3 = (4/3)*pi*(D/2)^3
#Volume of cylinder = pi r^2 h
#Multiple as required and output print statement

##------------------------------------------------## 

def area_square(side_length):
    area=side_length**2
    print('The area of a square with a side length of {} is: \n{}\n'.format(side_length,area))

def volume_cube(side_length):
    volume=side_length**3
    print('The volume of a cube with a side length of {} is: \n{}\n'.format(side_length,volume))
 

def area_circle(diameter,pi_value):
     area=pi_value*diameter
     print('The area of a circle with a diameter of {} is: \n{}\n'.format(diameter,area))


def volume_sphere(diameter,pi_value):
     volume=(4/3)*pi_value*((diameter/2)**3)
     print('The volume of a sphere with a diameter of {} is: \n{}\n'.format(diameter,volume))


def volume_cylinder(diameter,pi_value):
     volume=pi_value*((diameter/2)**2)*(diameter)
     print('The volume of a cylinder with a diameter of {} and a height of {} is: \n{}\n'.format(diameter,diameter,volume))


def job(length,pi_value):
    print(f"The length is: {length} \n")
    area_square(length)
    volume_cube(length)
    area_circle(length,pi_value)
    volume_sphere(length,pi_value)
    volume_cylinder(length,pi_value)

student_no=143950.76
pi_value=3.1415927

job(student_no,pi_value)