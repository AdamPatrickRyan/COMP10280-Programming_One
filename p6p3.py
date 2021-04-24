##------------------Practical 6 HW4----------------##
## 
##User:     Aryan
##DC:       2020-10-08
##DLM:      2020-10-08
##MC:       COMP10280
##SD:       Name check
##
##------------------Practical 6 HW4----------------## 

##------------------Algorithm----------------------## 

#if no error:
#Check name
##If first letter matches A, M, S, check if it's Adam/Spongebob/etc -> Quicker for string comparison
###If it passes the first letter check, check the whole string. If match print statement else print compliment statement
##if it doesnt then print the compliment

##------------------------------------------------## 

#Static values
print_myname="That is a cool name!"
print_doubtname="I'm not sure {} is your name..."
print_complname="You have a nice name."

#Not stripping whitespace just capitalisation

my_name="Adam Ryan"
my_name_ch=my_name.lower() 
my_name_l1=my_name_ch[0] #A

mm_name="Mickey Mouse"
mm_name_ch=mm_name.lower() 
mm_name_l1=mm_name_ch[0] #M

ss_name="Spongebob Squarepants"
ss_name_ch=ss_name.lower()
ss_name_l1=ss_name_ch[0] #S

entered_name=input("Please enter your full name: ")
entered_name_ch=entered_name.lower()
entered_name_l1=entered_name_ch[0]

#first letter match
if my_name_l1==entered_name_l1:

    #check the string
    if my_name_ch==entered_name_ch:
        print(print_myname)

    #not my name
    else:
        print(print_complname)

#first letter match
elif mm_name_l1==entered_name_l1:

        #check the string
        if mm_name_ch==entered_name_ch:
            print(print_doubtname.format(mm_name))
        
        #different name
        else:
            print(print_complname)

#first letter match
elif ss_name_l1==entered_name_l1:

        #check the string
        if ss_name_ch==entered_name_ch:
            print(print_doubtname.format(ss_name))

        #different name
        else:
            print(print_complname)

#no match on first letter
else:
    print(print_complname)
