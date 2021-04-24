##------------------Practical 6 HW4----------------##
## 
##User:     Aryan
##DC:       2020-10-08
##DLM:      2020-10-08
##MC:       COMP10280
##SD:       Password check
##
##------------------Practical 6 HW4----------------## 

##------------------Algorithm----------------------## 

#While the counter is less than three, ask for input.
#After input add 1 onto the counter
#If limit reached print error

##------------------------------------------------## 

#Static values
plaintext_password='Salesforce1!'
password_entry_limit=3
login_message='You have been successfully logged in.'
denied_message='You have been denied access'

password_entry_counter=0

while password_entry_counter<password_entry_limit:
    entered_password=input('Please enter the password: ')
    
    #Check password before adding to counter
    if entered_password==plaintext_password:
        print(login_message)
        exit()

    password_entry_counter+=1


if password_entry_counter==password_entry_limit:
    print(denied_message)
    
exit()