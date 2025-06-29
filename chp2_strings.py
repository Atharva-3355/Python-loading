# aj hum sikhenge strngs

string = "This is a String"
print(string)

# strings and variables should be named such that they are easyy to understandd soo that no no confusion aaye

# Example:

course = "Python Programming"

letter1 = course[0]  # Kyuki intex of 1st letter is 0
print("\n1st letter of the String: ", letter1)
letter2 = course[1]  # index of 2nd letter is 1.
print("2nd letter of the string: ", letter2)
letter3 = course[2]  # index of 3rd letter is 2
print("3rd letter of the string: ", letter3)

last_letter = course[-1]  # last letter (index before 0)
print("\nThe last letter of string: ", last_letter)
second_last_letter = course[-2]
# 2nd last letter (index before 0)
print("The Second last letter of string", second_last_letter)

first_3_letters = course[0:3]  # storing the 1st 3 letters in a variable
# then printing that variable
print("\nFirst 3 letters are: ", first_3_letters)

# directly printing the letters of 1st word
print("First 7 letters are:", course[0:6])

letter_from1 = course[0:]  # to take all letters starting from zero to last
letter_from2 = course[1:]  # to take all letters starting from 1st letter
letter_from3 = course[2:]  # to take all letters starting from 2nd letter
print("\nAll letters starting from 1st letter: ", letter_from1)
print("All letters starting from 2nd letter: ", letter_from2)
print("All letters starting from 3rd letter: ", letter_from3)


letter_till7 = course[:7]  # to take 1st 7 letters
letter_till11 = course[:11]  # to take 1st 11 letters
letter_till17 = course[:17]  # first 17 letters
print("\nFirst 7 letters: ", letter_till7)
print("First 11 letters: ", letter_till11)
print("First 17 letters: ", letter_till17)

# Some thing different:
copy_of_orignal = course[:]
print(course[:])  # prints the copy of orignal string


# Letss try some string handling functions

# 1) To take the length of a string we can use len as follows:

string_length = len(course)  # storing in a variable
print(string_length)  # then printing

print(len(course))  # directly printing
