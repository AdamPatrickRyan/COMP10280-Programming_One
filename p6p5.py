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

#While the counter is less than limit (1), ask for input.
#Check if password and if yes login
#After input add 1 onto the counter
#If limit reached require three correct entries.
##If entered login else deny

##------------------------------------------------## 

#Static values
plaintext_password='Salesforce1!'
password_entry_limit=1
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
    #Entered wrong the first time

    attempt_1=input('Please enter the password: ')
    attempt_2=input('Please enter the password: ')
    attempt_3=input('Please enter the password: ') 

    #note: check after all three are entered - don't validate password entry each attempt i.e. don't give info by informing which attempt is wrong

    #if all are equal then logged in
    if attempt_1==attempt_2==attempt_3==plaintext_password:
        print(login_message)
        exit()
    
    #denied
    else:
        print(denied_message)
        exit()