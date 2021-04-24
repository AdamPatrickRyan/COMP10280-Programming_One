##------------------Practical P18Q1----------------##
## 
##User:     Aryan
##DC:       2020-10-27
##DLM:      2020-10-27
##MC:       COMP10280
##SD:       Practical - Palindrome Iterative
##
##------------------Practical P18Q1----------------## 


##------------------Algorithm----------------------## 

#Note: I am not ignoring non-letters.

#Strip case.
#Find length to loop: half string.
#Default result as true.
#If letters match index +1 otherwise result=false and break string.
#If palindrome index exceeds but result is still true so done.



##------------------------------------------------## 

#Program to check whether a string is a palindromes
# # Prompts the user for strings and checks each one
# # Exits when an empty string is entered

def isPalindrome(s):
    """Checks whether the string s is a palindrome

Assumes s is a str.
Returns True if the letters in s form a palindrome;
Returns False otherwise.
Case is ignored, non-letters are not"""

    print(f"In isPalindrome('{s}'):")

    #Remove Case
    s=s.lower()

    #Loop length
    length_s=len(s)
    check_range=len(s)//2+1
    #Note: Only need to check half of the letters e.g. "abba" - need to chck [0]=[3]. [1]=[1]. 
    
    #Static
    letter_index=0
    Result=True

    if length_s>1:
        #Only need to check if length>1

        while letter_index<=check_range and Result:
            #in range to check and still palindrome

            neg_index=(-1*letter_index) - 1 #negative indexes start at -1 so need to do [0]=[-1], [1]=[-2] etc.
            #could also do it as length-index-1. Eg length=4, 0=3, 1=2

            if s[letter_index]==s[neg_index]:
                #letters are equal
                print(f'Letters being check are: s[{letter_index}]=s[{neg_index}] == {s[letter_index]} = {s[neg_index]}')

                #next letter
                letter_index+=1

            else:
                #Letter doesn't match
                print(f'Letters being check are: s[{letter_index}]!=s[{neg_index}] == {s[letter_index]} != {s[neg_index]}')

                #breaks loop
                Result=False

    print(f"IsPalindrome('{s}') check complete")
    return Result

user_input = input('Enter a string (empty string to exit):  ')



#Note I presume we need this as we were asked in the previous isPal function, but the answer is the function above.
while user_input != '':
    if isPalindrome(user_input):
        print('\nResult:') #tidy - could do as f string
        print(user_input, 'is a palindrome')
    else:
        print('\nResult:') #tidy - could do as f string
        print(user_input, 'is not a palindrome')
        
    user_input = input('Enter a string (empty string to exit):  ')

print('Finished')