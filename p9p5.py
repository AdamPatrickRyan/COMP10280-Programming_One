##------------------Practical P9Q5----------------##
## 
##User:     Aryan
##DC:       2020-10-15
##DLM:      2020-10-15
##MC:       COMP10280
##SD:       Practical - Pizza combinatorics
##
##------------------Practical P9Q5----------------## 


##------------------Algorithm----------------------## 


#Assuming we're not allowed use functions still which makes this a bit repetitive.

#Get number of ingredients
#Number of toppings
#Check if valid entries
#if so
    #ing-top
    #get factorial of each
    #get binomial coefficient
    #print

#Formula which is better to use: * from 1 to k of (n+1-i)/i [cancellation drops most terms below and large values memory heavy]


##------------------------------------------------## 

#Static values
int_ingredients=int(input("Please enter the number of unique topping ingredients: "))
int_topping_possibilities=int(input("Please enter the number of toppings allowed on the pizza: "))

#I don't entirely get this? I presume it means e.g. 5 toppings and 3 are allowed on the pizza?

if 0<=int_topping_possibilities<=int_ingredients:
    #must be between zero and n; nc0=1
    inglesstop=int_ingredients-int_topping_possibilities

    #Factorial counter for each
    fact_ing=1
    fact_top=1
    fact_inglesstop=1

    #Begin Factorial
    for ing_counter in range(1,int_ingredients+1):
        fact_ing*=ing_counter

    for top_counter in range(1,int_topping_possibilities+1):
        fact_top*=top_counter

    for inglesstop_counter in range(1,inglesstop+1):
        fact_inglesstop*=inglesstop_counter

    numerator=fact_ing
    denominator=fact_inglesstop*fact_top

    #Calculate Bc
    ingCtop=int(numerator/denominator) #binomial coefficients are ints and I don't want a decimal after.

    print("The total number if combinations of {} ingredients and {} toppings is: {}".format(int_ingredients,int_topping_possibilities,ingCtop))

else:
    print("You can't make pizzas with {} ingredients and {} topping choices".format(int_ingredients,int_topping_possibilities))
