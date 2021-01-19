"""
Project Title: Find the character of an ASCII code

Project Date: 01/17/2021

Project Description: Write a program that receives an ASCII
code (an integer between 0 and 127) and displays
its character. For example, if the user enters 97, the
program displays the character a.
"""

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

"""
Current obstacle: the user enters a non-number string.
Solutions: none, as of 7:26am, 1/19/2021
"""

# Output: The character is E

print("And now, for my next trick, give me a number, between 0 and 127.")
print("In exchange, I will make a letter appear in its place.")

presto = input("Give me a number, any number, between 0 and 127: ")
if str(presto):
    print("Psst.")
    print("I need the number, not the word for the number.")
    input("Give me a number, between 0 and 127, please: ")
else:
    chango = int(presto)
    if chango < 0:
        input("Give me a number, between 0 and 127, please: ")
    elif chango > 127:
        input("Give me a number, between 0 and 127, please: ")
    else:
        print("Voila!")
        print(chr(chango))
