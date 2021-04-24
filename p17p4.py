##------------------Practical P17Q4----------------##
## 
##User:     Aryan
##DC:       2020-10-27
##DLM:      2020-10-27
##MC:       COMP10280
##SD:       Practical - Palindrome
##
##------------------Practical P17Q4----------------## 


##------------------Algorithm----------------------## 

#Code from lecture
#toChar strips nonalphabets This is surely false as "tnsisn't" would be listed as a palindrome but it's not?
#
#isPal compares subsequent first and last characters and goes through string towards centre

#input, check if blank, run isPalindrome, request input, done



##------------------------------------------------## 

#Program to check whether a string is a palindromes
# # Prompts the user for strings and checks each one
# # Exits when an empty string is entered

def isPalindrome(s):
    """Checks whether the string s is a palindrome

Assumes s is a str.
Returns True if the letters in s form a palindrome;
Returns False otherwise.
Case and non-letters are ignored."""

    def toChars(s):
        """Converts a string to lowercase and removes non-letters
    
    Assumes s is a str.Converts uppercase letters to lowercase and removes non-letters."""
    # First of all, convert uppercase letters to lowercase

        s = s.lower()
        # Start with an empty stringl
        letterstring = ''

        # Go through s..
        for c in s:
            # ...  and add the character to the string if it is a letter
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letterstring += c

        return letterstring

    def isPal(s):
        """Checks whether the string s is a palindrome
        
        Assumes that s is a str with only lowercase letters and nonon-letters.
        Returns True if s is a palindrome;
        Returns False otherwise.Recursive function."""
        
        if len(s) <= 1:
            # A palindrome of length 0 or 1 is a palindrome
            return True
        else:
            # Compare the first and the last letters and check the remainder of the stringreturn 
            return s[0] == s[-1] and isPal(s[1:-1])


    return isPal(toChars(s))

user_input = input('Enter a string (empty string to exit):  ')

while user_input != '':
    if isPalindrome(user_input):
        print(user_input, 'is a palindrome')
    else:
        print(user_input, 'is not a palindrome')
        
    user_input = input('Enter a string (empty string to exit):  ')

print('Finished')