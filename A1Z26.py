# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# A1Z26 Cipher

def encode(plaintext):
    """Encode plaintext using A1Z26 cipher"""
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Convert alphabetic characters to their corresponding numerical values
            value = ord(char.upper()) - 64
            ciphertext += str(value) + "-"
        elif char.isdigit():
            # Leave digits as they are
            ciphertext += char
        else:
            # Ignore other characters
            pass
    # Remove the last hyphen
    ciphertext = ciphertext[:-1]
    return ciphertext

def decode(ciphertext):
    """Decode ciphertext using A1Z26 cipher"""
    plaintext = ""
    numbers = ciphertext.split("-")
    for number in numbers:
        if number.isdigit():
            # Convert numerical values to their corresponding alphabetic characters
            value = int(number) + 64
            plaintext += chr(value)
        else:
            # Leave hyphens as they are
            plaintext += "-"
    return plaintext

# Test the functions
plaintext = input("Enter text: ")
ciphertext = encode(plaintext)
print("Ciphertext:", ciphertext)

ciphertext_input = input("Enter ciphertext: ")
decoded_text = decode(ciphertext_input)
print("Decoded text:", decoded_text)
