##------------------Practical 5 HW3----------------##
## 
##User:     Aryan
##DC:       2020-10-06
##DLM:      2020-10-06
##MC:       COMP10280
##SD:       County relation
##
##------------------Practical 5 HW3----------------## 

##------------------Algorithm----------------------## 

#Get input
#Convert to lowercase to ensure dublin, Dublin, DUBlin, etc. work
#Check if input county is one of those in Leinster, then Munster, Conn, Leinster - use or statements as that's where we are in lecture
#If all elif statements fail it's not a known city

##------------------------------------------------## 


input_value=input("Please enter a city to check what region it's in: ")

#Make sure capitalisation does not matter - Convert all to lower case.
###Note: If looking for capitalisation to matter then capitalise first letter in county strings below
input_city=input_value.lower()

leins='Leinster'
Dublin_C='dublin' #Leinster
Kilkenny_C ='kilkenny' #Leinster

munst='Munster'
Cork_C='cork' #Musnter
Limerick_C ='limerick' #Munster
Waterford_C='waterford' #Munster

ulst='Ulster'
Belfast_C='belfast' #Ulster
Derry_C='derry' #Ulster
Lisburn_C ='lisburn' #Ulster

conna='Connaught'
Galway_C ='galway' #Connaught
Sligo_C='sligo' #Connaught



#Leinster
if input_city==Dublin_C or input_city==Kilkenny_C:
    print('You entered {}. {} is in {}'.format(input_value,input_value,leins))

#Munster
elif input_city==Cork_C or input_city==Limerick_C or input_city==Waterford_C:
    print('You entered {}. {} is in {}'.format(input_value,input_value,munst))

#Connaught
elif input_city==Galway_C or input_city==Sligo_C:
    print('You entered {}. {} is in {}'.format(input_value,input_value,conna))

#Ulster
elif input_city==Belfast_C or input_city==Derry_C or input_city==Lisburn_C:
    print('You entered {}. {} is in {}'.format(input_value,input_value,ulst))

#Not known
else:
    print('Sorry, I didn’t recognise that name.')