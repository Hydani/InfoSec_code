"""
UTA CSE 4381-001 Information Security II / Homework 1
Submission Date: 09.11.2023

Name: Hyeonjun An
Student ID: 1001342487
"""

import random as rd
import string

def genRandomKey(str:string):
    """
    Generate a random key pad of the same length as the plain text.
    """
    return "".join(rd.choice(string.printable) for _ in str)

def encrypt(str:string, key:string):
    """
    Encrypt the plain text to a new cipher text by raising the plain text in unicode value to the power of the random pad generated.
    ord() - string to a single Unicode character and return its integer Unicode value.
    chr() - integer to a string representing a character at the Unicode value.
    """
    return "".join(chr(ord(i) ^ ord(j)) for (i, j) in zip(str, key))

def decrypt(cipherText:string, key:string):
    """
    Decryption occurs in the reverse direction of encryption.
    """
    return encrypt(cipherText, key)


if __name__ == "__main__":
    print("Please type in your text to be encrypted.")
    plain_text = input()
    if (not len(plain_text)): #Check if the input is empty.
        print("Please Type in the text you wish to encrypt.")
        exit(0)

    cipher_text = []
    original_text = []

    key = genRandomKey(plain_text)

    cipher_text = encrypt(plain_text, key)
    print("Your cipher text is below:")
    print(cipher_text)

    original_text = decrypt(cipher_text, key)
    print("Your decrypted text is below:")
    print(original_text)
