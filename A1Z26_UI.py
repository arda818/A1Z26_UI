# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 19:06:35 2023

@author: ardam
"""

import tkinter as tk

# A1Z26 Cipher functions
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

# Create the GUI
root = tk.Tk()
root.title("A1Z26 Cipher")

# Create the input label and text box
input_label = tk.Label(root, text="Enter text to encode/decode:")
input_label.pack()
input_text = tk.Text(root, height=10, width=50)
input_text.pack()

# Create the encode button
def encode_text():
    plaintext = input_text.get("1.0", "end-1c")
    ciphertext = encode(plaintext)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", ciphertext)

encode_button = tk.Button(root, text="Encode", command=encode_text)
encode_button.pack()

# Create the decode button
def decode_text():
    ciphertext = input_text.get("1.0", "end-1c")
    plaintext = decode(ciphertext)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", plaintext)

decode_button = tk.Button(root, text="Decode", command=decode_text)
decode_button.pack()

# Create the output label and text box
output_label = tk.Label(root, text="Encoded/Decoded text:")
output_label.pack()
output_text = tk.Text(root, height=10, width=50)
output_text.pack()

# Start the GUI
root.mainloop()
