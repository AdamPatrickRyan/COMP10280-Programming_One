##------------------Practical P17Q3----------------##
## 
##User:     Aryan
##DC:       2020-10-27
##DLM:      2020-10-27
##MC:       COMP10280
##SD:       Practical - Cats and Dogs
##
##------------------Practical P17Q3----------------## 


##------------------Algorithm----------------------## 

#Input

#F1: Function to count how many times if a term is in a string
#F2: Function to check if two terms are in a string an equal number of times

#input
#if equal print one statement, else print another statment



##------------------------------------------------## 

def search_string_count(string_to_search,search_term):
    """Returns the count of a string in another string

    Enter string to search, search string"""

    #do not alter case etc

    str_count=string_to_search.count(search_term)

    return str_count

def two_string_search_comparison(string_to_search,search_term_1, search_term_2):
    """Returns if two search term appears an equal number of times in a string 

    Enter string to search and search terms, search string"""

    output=False
    str_1_count=string_to_search.count(search_term_1)
    str_2_count=string_to_search.count(search_term_2)

    if str_1_count==str_2_count:
        #returns true if yes otherwise false
        output=True

    #could output as a list if needed counts

    return output

#terms to search - static
cat_str='cat'
dog_str='dog'

string_to_search=input("Please enter a case-sensitive sentence to see if there's an equal presence of 'cat' and 'dog' in the sentence: ")



if two_string_search_comparison(string_to_search,cat_str,dog_str):
    #true if yes
    print_statement=f'{cat_str} and {dog_str} appear an equal number of times in your sentence'
else:
    #false if not
    print_statement=f'{cat_str} and {dog_str} do not appear an equal number of times in your sentence'

print(print_statement)