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
Current obstacle: add code to avoid the viola function if chango fails num_check
Solutions: none, as of 9:05pm, 1/24/2021
"""

# Output: The character is E


def num_check(chango):
    """
    """

    print("What do we have here?")
    if chango < 0:
        print("What's this? This number is too small!")
    elif chango > 127:
        print("What's this? This number is too big!")


def voila(chango):
    """
    """

    print("Voila!")
    print(chr(chango))


if __name__ == "__main__":
    """
    """

    print("And now, for my next trick, give me a number, between 0 and 127.")
    print("In exchange, I will make a letter appear in its place.")

    presto = input("Give me a number, any number, between 0 and 127: ")

    try:
        chango = int(presto)

    except ValueError as err:
        print("INFO: Could not convert data into a integer.")
        print("DEBUG: {0}".format(err))

        exit()

    num_check(chango)
    voila(chango)
