##------------------Practical P16Q1----------------##
## 
##User:     Aryan
##DC:       2020-10-27
##DLM:      2020-10-27
##MC:       COMP10280
##SD:       Practical - Another Recursion
##
##------------------Practical P16Q1----------------## 


##------------------Algorithm----------------------## 

#Two functions:
#f_recur: Prints the sequence given a number of terms:
##f(n): Calculates the nth term of sequence.

#while input>=1:
#f_recur is called:
##if terms in 1 then answer is easy so print immediately
##otherwise we need to get f(x) for x in (2,3,...)
###for x in list
####call f(n) which calculates the series as given recursively
####Append f(n) to string
#Done so ask again.

##------------------------------------------------## 


###This is almost identical to the code I've used for all of the recursive functions with some minor modifications as the only thing that's needed to be updated is f(n) and terms definitions.

def f_recur(terms):
    """Function to print the Sequence


    Terms>0. Prints that number of terms."""

    print(f'In f_recur({terms}):\n')

    #######------Function for f(n)---------######    
    def rf(n):
        f"""Series nth term
        
        Calculates he nth term. Highly highly inefficient
        """

        print(f'In f({n}):\n')


        f0=2

        if n==1:
            #base case
            print('base case: f(1)=2')
            return f0

        else:
            #n is 2+ which means fn is 2*f(n-1)

            print(f'Checking f({n-1}):')
            f_n_min_1=rf(n-1)
            print(f"f({n-1})={f_n_min_1}")
            f_n=(2*(f_n_min_1))


            print('\n\n --- \n\nValues found:')
            print(f'f({n})=2(f({n-1}))=2*{f_n_min_1}={f_n}\n\n')
            return f_n
    
    #######-----End of fn----##########

    #static
    f0=2

    print_statement='The Series is: '

    if terms<1:
        print(f'{terms} terms does not make sense. Please choose a number >0.')
        return
    else:
        print_statement+='{}'.format(f0)

        #three + terms - need to find the values of f sequence. If terms = 3, then we want value of f(terms-2). Start with f(2) which is third term.
        for counter in range(2,terms+1):
            print('Looping through f values: ')
            f_n=rf(counter)
            print_statement+=', {}'.format(f_n)
            print(f'Appended f({counter}) to string')
    
        print(print_statement)
        return


        
terms=int(input('Please enter a number of terms >=1 to get of the sequence:  '))

while terms>=1:
    #non-negative
    f_recur(terms)

    #ask again
    terms=int(input('Please enter another number of terms >=1 to get of the sequence:  '))

else:
    print(f'Terminated as you entered {terms} which is <1')