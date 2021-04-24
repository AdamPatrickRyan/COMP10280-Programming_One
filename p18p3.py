##------------------Practical P18Q3----------------##
## 
##User:     Aryan
##DC:       2020-10-29
##DLM:      2020-10-29
##MC:       COMP10280
##SD:       Practical - Code count
##
##------------------Practical P18Q3----------------## 


##------------------Algorithm----------------------## 

#This is a bit trickier.

#code_check function works as:
#Get length of input

#get length of allowed prefix
##co=2

#get length of allowed suffix
##d=1

#get length of allowed mid-section
##e.g. 'd'=1.

#find the total length of what we want to check = prefix+suffix+mid section
##co+d+e = 4

#if the length we want to check is larger than the string 0, otherwise

#for every piece of the search string that's prefix+suffix+mid section long:
#check if the start of the slice is preffix, if the end is the suffix, and if every character in the mid sectionis in the allowed alphabet, add to count.

#return the total count.

##generalised.


##------------------------------------------------## 


def code_check(s,prefix,suffix,mid_length,allowed_list):
    """Checks whether the string contains co{letter}e.
    
    Input: 
    string
    case sensitive prefix to check for
    case sensitive suffix to check for
    the length of characters to allow in between prefix and suffix
    the characters allowed between prefix and suffix to still return true
    """

    #if you can use regex it's easier, but avoiding it as we didn't improt re in module


    #lengths of sections rename
    length_s=len(s)

    start_s=prefix
    length_preffix=len(start_s)

    length_mid_s=mid_length

    end_s=suffix
    length_suffix=len(end_s)

    #legnth of string to check for=4
    total_check_length=length_preffix+length_suffix+length_mid_s

    #default not found =0
    count=0

    if length_s>=total_check_length:
        #string is more than what we're checking
        check_range=length_s - total_check_length + 1 #max string - legnth of check string +1 to cover final bit

        for index in range(check_range):
            #up to the end of the string - check length

             
            max_slice_index= index + total_check_length
            ##e.g. 4 implies want to check 0 to 3, 1 to 4, etc.
            
            
            #slice to examine for our string
            check_slice=s[index:max_slice_index]


            print(f"\n\nCurrently checking the following letters: {check_slice}")

            #start letters
            check_slice_prefix=check_slice[0:length_preffix]

            #end letters
            check_slice_suffix=check_slice[-1*(length_suffix):]

            #from prefix up to end of check section
            check_slice_mid=check_slice[length_preffix:length_preffix+length_mid_s]


            print(f"In this segment we are checking these letters for your prefix: {check_slice_prefix}=={start_s}? {check_slice_prefix==start_s}")
            print(f"In this segment we are checking these letters for your suffix: {check_slice_suffix}=={end_s}? {check_slice_suffix==end_s}")
            print(f"\n\nIn this segment we are checking if this {check_slice_mid} is in the allowed characters: {allowed_list}")

            #assume in allowed list
            mid_check=0

            for letter in check_slice_mid:
                #validate allowed letter

                if letter not in allowed_list:
                    mid_check+=1

            #if any letter in the mid section is not in the allowed list than mid_check>0 also check prefix+suffix
            if check_slice_prefix==start_s and check_slice_suffix==end_s and mid_check==0:
                print(f"Start and end match and middle in allowed characters! Count+1")
                count+=1

    return count

def job():
    pre='co'
    suf='e'
    mid_length=1 #how many letters do you want to allow? e.g. co---e is accepted? co-e is accepted? etc.

    allowed_mid_section='abcdefghijklmnopqrstuv'+'abcdefghijklmnopqrstuv'.upper()

    user_input = input("Enter a case-sensitive string to count 'co(letter)e':  ")
    code_count=code_check(user_input,pre,suf,mid_length,allowed_mid_section)

    if code_count==1:
        x='.'
    else:
        x='s.'

    print("In your string 'co(letter)e' appears"+f": {code_count} time{x}")

job()