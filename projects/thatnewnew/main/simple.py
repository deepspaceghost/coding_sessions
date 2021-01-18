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

as_key = input(int("Hand over the ASCII!: "))
if as_key is < 0 or > 127:
	print("Can you read?")
	print("I need a number between 0 and 127.")
else:
    print("Good job! Go get yourself cookie.")
    print()
