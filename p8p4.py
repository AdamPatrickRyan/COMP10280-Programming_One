##------------------Practical P8Q4----------------##
## 
##User:     Aryan
##DC:       2020-10-15
##DLM:      2020-10-15
##MC:       COMP10280
##SD:       Practical - Range again.
##
##------------------Practical P8Q4----------------## 


##------------------Algorithm----------------------## 


#Get input, check which range it's in. If not in first move to second etc., get counter for each range, print, repeat.
#Reusing code from p5p4 as it's almsot exactly the same question.

##------------------------------------------------## 

#Static values
int_user_input=int(input("Please enter a number to check what range it's in: "))

#Group maximums
max_range_g1=0
max_range_g2=20
max_range_g3=40
max_range_g4=60
max_range_g5=80
max_range_g6=100

g1_counter=0 #0
g1g2_counter=0 
g2g3_counter=0
g3g4_counter=0
g4g5_counter=0
g5g6_counter=0
g6p_counter=0

#Main prints
mingroup_print_statement='Number is equal to {}'
group_print_statement="Number is greater than {} and less than or equal to {}"
maxgroup_print_statement='Number is greater than {}'

#NegativeEnding
ending_statement='You entered {} which is less than {}. Ending now'

#Analysis
minanalysis_line_statement="You entered {} numbers which were equal {}"
mainanalysis_line_statement="You entered {} numbers between {} and {}"
maxanalysis_line_statement="You entered {} numbers which are greater than {}"

#Renter number print
renter_print="Please enter another non-negative number to check what range it's in, or a negative number to stop: "

#Not less than min bound
while int_user_input>=max_range_g1:
#Group 1 - 0
    if int_user_input==max_range_g1 :
        print(mingroup_print_statement.format(int_user_input))
        g1_counter+=1

    #Group 2 - 0 to 20
    elif max_range_g1<int_user_input<=max_range_g2:
        g1g2_counter+=1
        print(group_print_statement.format(max_range_g1,max_range_g2))

    #Group 3 - 20 to 40
    elif max_range_g2<int_user_input<=max_range_g3:
        g2g3_counter+=1
        print(group_print_statement.format(max_range_g2,max_range_g3))

    #Group 4 - 40 to 60
    elif max_range_g3<int_user_input<=max_range_g4:
        g3g4_counter+=1
        print(group_print_statement.format(max_range_g3,max_range_g4))

    #Group 5 - 60 to 80
    elif max_range_g4<int_user_input<=max_range_g5:
        g4g5_counter+=1
        print(group_print_statement.format(max_range_g4,max_range_g5))

    #Group 6 - 80 to 100
    elif max_range_g5<int_user_input<=max_range_g6:
        g5g6_counter+=1
        print(group_print_statement.format(max_range_g5,max_range_g6))

    #Group 7 - 100+
    elif int_user_input>max_range_g6:
        g6p_counter+=1
        print(maxgroup_print_statement.format(max_range_g6))


    int_user_input=int(input(renter_print))
    

#Group 0 - Less than 0
else:
    print(ending_statement.format(int_user_input,max_range_g1))

final_statement_1=minanalysis_line_statement.format(g1_counter, max_range_g1)
final_statement_2=mainanalysis_line_statement.format(g1g2_counter,max_range_g1,max_range_g2)
final_statement_3=mainanalysis_line_statement.format(g2g3_counter,max_range_g2,max_range_g3)
final_statement_4=mainanalysis_line_statement.format(g3g4_counter,max_range_g3,max_range_g4)
final_statement_5=mainanalysis_line_statement.format(g4g5_counter,max_range_g4,max_range_g5)
final_statement_6=mainanalysis_line_statement.format(g5g6_counter,max_range_g5,max_range_g6)
final_statement_7=maxanalysis_line_statement.format(g6p_counter,max_range_g6)
final_statement_8="You entered 1 number less than {} to stop the program.".format(max_range_g1) #True condition to end outside of error i.e. conversion

final_print="While entering numbers into this program:\n\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n".format(final_statement_1,final_statement_2,final_statement_3,final_statement_4,final_statement_5,final_statement_6,final_statement_7,final_statement_8)

print(final_print)