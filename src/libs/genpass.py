# DONE!!!

# This library is created for project merlin and it's licensed under the MIT license.
# We need some numbers
# We need some characters -> We need to import strings library for this. 
# We need some special characters
# We need a combine function to combine the numbers with characters
# We need to create a secure string that will not that no two processes can obtain the same data simultaneously.

import secrets
import string


def generate(length) -> str:
    # First abort the password generation if the length
    # of the password is less than 8
    if length < 8:
        exit("This tool will not generate a password less than 8 characters.")

    # Add the letters
    letters = string.ascii_letters

    # Add the numbers
    numbers = string.digits
    
    # Add the special characters
    specials = string.punctuation
    
    # Create a superset of characters 
    allChars = letters + numbers + specials
    
    # Then securely create the random password
    password = ''.join((secrets.choice(allChars) for x in range(length)))

    # And after all, return the password.
    return password



