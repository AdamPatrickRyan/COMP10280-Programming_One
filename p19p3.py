##------------------Practical P19Q3----------------##
## 
##User:     Aryan
##DC:       2020-10-29
##DLM:      2020-10-29
##MC:       COMP10280
##SD:       Practical - Count of characters
##
##------------------Practical P19Q3----------------## 


##------------------Algorithm----------------------## 


#Identical to p18p6.

#check if input exists
#read input
#count input letters
#check if balanced
#output file in dir.

##------------------------------------------------## 

import os

def str_read_file(file_name):
    """Assumes in same file path, reads in the file"""

    file = open(file_name, 'r')
    str_file=file.read()
    file.close()

    return str_file


def validate_filepath(file_name):
    """Assumes in same file path, checks if exists note: Not a good way of doing this!"""

    check=os.path.isfile(file_name)

    return check


def write_output_filepath(output_path,string_write):
    """Write output file - if not exist it makes the file"""

    file = open(output_path, 'w+') #w+ to make if not exist
    write=file.write(string_write)
    file.close()

    return



def count_words(file_name):
    """Counts the words in the file"""
    str_file=str_read_file(file_name)

    l1='('
    l2=')'

    l3='['
    l4=']'

    l10='{'
    l11='}'

    l5='<'
    l6='>'

    l7='\n'
    l8='<!-- and the string -->'
    l9='e'


    count_1=0
    count_2=0

    count_3=0
    count_4=0

    count_5=0
    count_6=0

    count_7=0
    count_8=0
    count_9=0

    count_11=0
    count_10=0

    count_1=str_file.count(l1)
    count_2=str_file.count(l2)
    count_3=str_file.count(l3)
    count_4=str_file.count(l4)
    count_5=str_file.count(l5)
    count_6=str_file.count(l6)
    count_7=str_file.count(l7)
    count_8=str_file.count(l8)
    count_9=str_file.count(l9)
    count_10=str_file.count(l10)
    count_11=str_file.count(l11)

    balance=False

    if count_1==count_2 and count_3==count_4 and count_5==count_6 and count_11==count_10:
        balance=True

    print_statement=f"""
The counts are:
{l1}: {count_1}
{l2}: {count_2}
{l10}:{count_10}
{l11}:{count_11}
{l3}: {count_3}
{l4}: {count_4}
{l5}: {count_5}
{l6}: {count_6}
new lines: {count_7}
{l8}: {count_8}
{l9}: {count_9}
---
Are the brackets balanced (i.e. counts opening and closing match)?: {balance}
"""

    print(print_statement)

    return print_statement


def main_job(inputpath,outputpath):
    """Runs the job"""
    input_validator=validate_filepath(inputpath)

    if input_validator!=True:
        #no input
        print('Input file does not exist - cannot read file')
    
    else:
        #validated by writing if not exists; saving in same directory
        output_statement=count_words(inputpath)

        write_output_filepath(outputpath,output_statement)
    
    return

inp='index.html'
outp='results.txt'

main_job(inp,outp)



