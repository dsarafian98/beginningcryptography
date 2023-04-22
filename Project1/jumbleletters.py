# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 16:15:59 2020

@author: Danielle Sarafian and Fabien Debies
"""
import string
import random

def jumble_letters():
    alphabet = string.ascii_uppercase
    alphabet_size=len(alphabet)
    code = list(alphabet)
    
    #get random number and switch current letter with the letter at that index
    for i in range(alphabet_size):
        num = random.randint(0, alphabet_size-1)
        temp = code[i]
        code[i] = code[num]
        code[num] = temp
        
    #add new alphabet to dictionary
    encoding = {}
    decoding = {}
    for i in range(alphabet_size):
        letter = code[i]
        subst_letter = string.ascii_uppercase[(i)%alphabet_size]
        encoding[letter] = subst_letter
        decoding[subst_letter] = letter
    return encoding, decoding

def encode(message, subst):
    cipher = ""
    for letter in message:
        if letter in subst:
            cipher += subst[letter]
        else:
            cipher += letter
    return cipher

def decode(message, subst):
    return encode(message, subst)

def printable_substitution(subst):
    #Sort by source character so things are alphabetized.
    mapping = sorted(subst.items())
    
    #Then create two lines: source above, target beneath
    alphabet_line = " ".join(letter for letter, _ in mapping)
    cipher_line = " ".join(subst_letter for _, subst_letter in mapping)
    return "{}\n{}".format(alphabet_line, cipher_line)

if __name__ == "__main__":
    encoding, decoding = jumble_letters()
    while True:
        print("\nShift Encoder Decoder")
        print("---------------------")
        print("\t1. Print Encoding/Decoding Tables.")
        print("\t2. Encode Message.")
        print("\t3. Decode Message.")
        print("\t4. Jumble Letters.")
        print("\t5. Quit.\n")
        choice = input(">> ")
        print()
        
        if choice == '1':
            print("Encoding Table:")
            print(printable_substitution(encoding))
            print("Decoding Table:")
            print(printable_substitution(decoding))
            
        elif choice == '2':
            message = input("\nMessage to encode: ")
            print("Encoded Message: {}".format(encode(message.upper(), encoding)))
            
        elif choice == '3':
            message = input("\nMessage to decode:")
            print("Decoded Message: {}".format(decode(message.upper(), decoding)))
        
        elif choice == '4':
            encoding, decoding = jumble_letters()
            print("Current Code:\n")
            print(printable_substitution(encoding))
            print(printable_substitution(decoding))
            
        elif choice == '5':
            print("Terminating.\n")
            break
        
    else:
        print("Unknown option {}.".format(choice))
        