##------------------Practical P15Q1----------------##
## 
##User:     Aryan
##DC:       2020-10-22
##DLM:      2020-10-22
##MC:       COMP10280
##SD:       Practical - Recursion
##
##------------------Practical P15Q1----------------## 


##------------------Algorithm----------------------## 

#Two functions:
#f_recur: Prints the sequence given a number of terms:
##f(n): Calculates the nth term of sequence.

#while input>=1:
#fib_recur is called:
##if terms in 1 then answer is easy so print immediately
##otherwise we need to get f(x) for x in (2,...)
###for x in list
####call f(n) which calculates the series series as f(1)=2,f(n)=n+f(n-1)
####Append f(n) to string
#Done so ask again.

##------------------------------------------------## 


def f_recur(terms):
    """Function to print the Sequence


    Terms>1. Prints that number of terms."""

    print(f'In f_recur({terms}):\n')

    #######------Function for f(n)---------######    
    def f(n):
        f"""f nth term
        
        Calculates the nth term. Highly highly inefficient
        """

        print(f'In f({n}):\n')

        f1=1
        
        if n==1:
            print('base case: f(1)=2')
            return f1

        else:
            #n is 2+ which means fn is fn-1 + n
            f_n_min_1=f(n-1)
            print(f"f({n-1})={f_n_min_1}")
            f_n=f_n_min_1+2**(n-1)
            print('\n\n --- \n\nValues found:')
            print(f'f({n})={n}+f({n-1})={f_n_min_1}+{n}={f_n}\n\n')
            return f_n
    
    #######-----End of fn----##########

    #static
    f1=1

    print_statement='The Series is: '
    print_statement+='{}'.format(f1)

    if terms==1:
        print(print_statement)
        return

    else:
        #three + terms - need to find the values of fib sequence. If terms = 3, then we want value of f(terms-2). Start with f(2) which is third term.
        for counter in range(2,terms+1):
            print('Looping through series values: ')
            f_n=f(counter)
            print_statement+=', {}'.format(f_n)
            print(f'Appended f({counter}) to series')
    
        print(print_statement)
        return


        
terms=int(input('Please enter a number of terms >=1 to get of the sequence:  '))

while terms>=1:
    #non-negative
    f_recur(terms)
    #ask again
    terms=int(input('Please enter another number of terms >=1 to get of the sequence:  '))

else:
    print(f'Terminated as you entered {terms} which is <1.')