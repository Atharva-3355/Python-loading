# aj hum sikhenge strngs

string = "This is a String"
print(string)

# strings and variables should be named such that they are easyy to understandd soo that no no confusion aaye

# Example:

course = "Python Programming"

letter1 = course[0]  # Kyuki intex of 1st letter is 0
print(letter1)
letter2 = course[1]  # index of 2nd letter is 1
print(letter2)
letter3 = course[2]  # index of 3rd letter is 2
print(letter3)

last_letter = course[-1]  # last letter (index before 0)
print(last_letter)
second_last_letter = course[-2]
print(second_last_letter)  # 2nd last letter (index before 0)

first_3_letters = course[0:3]  # storing the 1st 3 letters in a variable
print("First 3 letters are: ", first_3_letters)  # then printing that variable

# directly printing the letters of 1st word
print("First 7 letters are:", course[0:6])


# Letss try some string handling functions

# 1) To take the length of a string we can use len as follows:

string_length = len(course)  # storing in a variable
print(string_length)  # then printing

print(len(course))  # directly printing
