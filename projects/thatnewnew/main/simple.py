'''
Project Title: Find the character of an ASCII code

Project Date: 01/17/2021

Project Description: Write a program that receives an ASCII
code (an integer between 0 and 127) and displays
its character. For example, if the user enters 97, the
program displays the character a.
'''

# Input: Enter an ASCII code: 69 [enter]

# Input constraints: Is the input an integer? Between 0 and 127?

# Compute

"""
To get the ASCII code of a character, use
the ord() function. To get the character encoded by
an ASCII code number, use the chr() function. To
know if all the characters present in a string
are alphanumeric i.e. they are alphabets and numeric, use
the isalnum() function.
"""

# Output: The character is E

print("And now, for my next trick...")
print("I will change your number into a letter.")

presto = input("Give me your number: ")

chango = int(presto)

print(chr(chango))
