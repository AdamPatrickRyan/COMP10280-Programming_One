##------------------Practical 2 HW1----------------##
## 
##User:     Aryan
##DC:       2020-09-29
##DLM:      2020-09-29
##MC:       COMP10280
##SD:       Index of strings
##
##------------------Practical 2 HW1----------------## 

animal='elephant'
length_animal=len(animal)

#Go through all of the letters
print('Going through all of the positive indices <= length \n')
for letter_num in range(length_animal):
    letter=animal[letter_num]
    print("The index is {}, and the {}th letter is {}".format(letter_num, letter_num,letter))

#Show what happens if index>length(string)
print('\nExperimenting with indices > length \n')
try:
    print("If I enter 10, I see: {}.".format(animal[10]))
except:
    print('Indice > Length result: This produces an error \n')

#Go through all of the letters backwards
print('Going through all of the negative indices where abs(index) <= abs(length) \n')
for i in range(1,length_animal+1):
    #+1 to get 0th letter
    letter_num=length_animal-i
    index=(-1)*i
    letter=animal[index]
    print("The index is {}, and the {}th letter is {}".format(index, letter_num,letter))

#Show what happens if index negative and abs(index)>length(string)
print('Experimenting with indices > length \n')
try:
    print("If I enter -10, I see: {}.".format(animal[-10]))
except:
    print('ABS(Index) > ABS(Length) result: This produces an error \n')

print('Experimentation complete! \n')

My_answer_as_text=f"""

Q4. If the index is positive and less than the length of the string, it returns the character in that position (zero-indexed):

The index is 0, and the 0th letter is e
The index is 1, and the 1th letter is l
The index is 2, and the 2th letter is e
The index is 3, and the 3th letter is p
The index is 4, and the 4th letter is h
The index is 5, and the 5th letter is a
The index is 6, and the 6th letter is n
The index is 7, and the 7th letter is t

If the Index > length of the string, it returns an error.

If the absolute value of the index is less than the length of the string, and the index is negative, it returns that character from the right of the string.

The index is -1, and the 7th letter is t
The index is -2, and the 6th letter is n
The index is -3, and the 5th letter is a
The index is -4, and the 4th letter is h
The index is -5, and the 3th letter is p
The index is -6, and the 2th letter is e
The index is -7, and the 1th letter is l
The index is -8, and the 0th letter is e

E.g. the first character from the end of the string "elephant" is t, so entering -1 returns t, while entering -5 returns p

If the absolute value of the index is greater than the length of the string + 1, and is negative then it returns an error
"""


print(My_answer_as_text)
