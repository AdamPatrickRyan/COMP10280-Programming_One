##------------------Practical P14Q5----------------##
## 
##User:     Aryan
##DC:       2020-10-22
##DLM:      2020-10-22
##MC:       COMP10280
##SD:       Practical - Fibonnacci Recursion
##
##------------------Practical P14Q5----------------## 


##------------------Algorithm----------------------## 

#Two functions:
#fib_recur: Prints the fibonacci sequence given a number of terms:
##fib(n): Calculates the nth term of fibaonnaci sequence.

#while input>=0:
#fib_recur is called:
##if terms in 0,1,2 then answer is easy so print immediately
##otherwise we need to get f(x) for x in (3,...)
###for x in list
####call f(n) which calculates the fibonacci series as f(0)=1,f(1)=1,f(n)=f(n-1)+f(n-2)
####Append f(n) to string
#Done so ask again.

##------------------------------------------------## 


def fib_recur(terms):
    """Function to print the Fibonacci Sequence


    Terms>0. Prints that number of terms."""

    print(f'In fib_recur({terms}):\n')

    #######------Function for f(n)---------######    
    def rfib(n):
        f"""Fibonacci nth term
        
        Calculates he nth term. Highly highly inefficient
        """

        print(f'In fib({n}):\n')


        f0=0
        f1=1

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
            fib_n_min_2=rfib(n-2)

            print(f'Checking f({n-1}):')
            fib_n_min_1=rfib(n-1)

            print(f"f({n-2})={fib_n_min_2}")
            print(f"f({n-1})={fib_n_min_1}")
            

            fib_n=fib_n_min_1+fib_n_min_2


            print('\n\n --- \n\nValues found:')
            print(f'f({n})=f({n-1})+f({n-2})={fib_n_min_1}+{fib_n_min_2}={fib_n}\n\n')
            return fib_n
    
    #######-----End of fn----##########

    #static
    f0=0
    f1=1

    print_statement='The Fibonacci Series is: '

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
            #three + terms - need to find the values of fib sequence. If terms = 3, then we want value of f(terms-2). Start with f(2) which is third term.
            for counter in range(2,terms):
                print('Looping through fibonacci values: ')
                fib_n=rfib(counter)
                print_statement+=', {}'.format(fib_n)
                print(f'Appended f({counter}) to Fibonacci string')
        
            print(print_statement)
            return


        
terms=int(input('Please enter a number of terms >1 to get of the Fibonnaci sequence:  '))

while terms>=0:
    #non-negative
    fib_recur(terms)

    #ask again
    terms=int(input('Please enter another number of terms >1 to get of the Fibonnaci sequence:  '))

else:
    print(f'Terminated as you entered {terms} which is non-positive.')