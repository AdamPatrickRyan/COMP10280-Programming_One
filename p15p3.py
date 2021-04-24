##------------------Practical P14Q5----------------##
## 
##User:     Aryan
##DC:       2020-10-22
##DLM:      2020-10-22
##MC:       COMP10280
##SD:       Practical - fonnacci Recursion
##
##------------------Practical P14Q5----------------## 


##------------------Algorithm----------------------## 

#Two functions:
#f_recur: Prints the sequence given a number of terms:
##f(n): Calculates the nth term of faonnaci sequence.

#while input>=0:
#Add term+1 to correct for 0 indexing.
#f_recur is called:
##if terms in 0,1,2 then answer is easy so print immediately
##otherwise we need to get f(x) for x in (3,...)
###for x in list
####call f(n) which calculates the series as given recursively
####Append f(n) to string
#Done so ask again.

##------------------------------------------------## 


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


        f0=13
        f1=8

        if n==0:
            #0
            print('base case: f(0)=0')
            return f0
        
        elif n==1:
            #1
            print('base case: f(1)=1')
            return f1

        else:
            #n is 2+ which means fn is fn-1 + fn-2

            print(f'Checking f({n-2}):')
            f_n_min_2=rf(n-2)

            print(f'Checking f({n-1}):')
            f_n_min_1=rf(n-1)

            print(f"f({n-2})={f_n_min_2}")
            print(f"f({n-1})={f_n_min_1}")
            

            f_n=(13*(f_n_min_1))+(f_n_min_2)


            print('\n\n --- \n\nValues found:')
            print(f'f({n})=13(f({n-1}))+f({n-2})=13*{f_n_min_1}+{f_n_min_2}={f_n}\n\n')
            return f_n
    
    #######-----End of fn----##########

    #static
    f0=13
    f1=8

    #this question asks for starting at '0th' term. Previously I've built for first, second, etc. so I'm adding 1 to the term to correct.
    #Remove this if you want the 'proper' first, second, etc. term.
    terms+=1 

    print_statement='The Series is: '

    if terms<1:
        print(f'{terms} terms does not make sense. Please choose a number >0.')
        return

    elif terms==1:
        print_statement+='{}'.format(f0)
        print(print_statement)
        return

    else:
        print_statement+='{}, {}'.format(f0,f1)

        if terms==2:
            #two terms - print statement is ready
            print(print_statement)
            return

        else:
            #three + terms - need to find the values of f sequence. If terms = 3, then we want value of f(terms-2). Start with f(2) which is third term.
            for counter in range(2,terms):
                print('Looping through f values: ')
                f_n=rf(counter)
                print_statement+=', {}'.format(f_n)
                print(f'Appended f({counter}) to string')
        
            print(print_statement)
            return


        
terms=int(input('Please enter a number of terms >=1 to get of the sequence:  '))

while terms>=0:
    #non-negative
    f_recur(terms)

    #ask again
    terms=int(input('Please enter another number of terms >=1 to get of the sequence:  '))

else:
    print(f'Terminated as you entered {terms} which is non-positive.')