# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 16:15:59 2020

@author: Danielle Sarafian and Fabien Debies
"""
import string
import random
import math

def create_code():
    alphabet = string.ascii_uppercase
    alphabet_size=len(alphabet)
    code = list(alphabet)
    
    #get random number and switch current letter with the letter at that index
    for i in range(alphabet_size):
        num = random.randint(0, alphabet_size-1)
        temp = code[i]
        code[i] = code[num]
        code[num] = temp
    return code
        
def encode(message, a, b, code):
    cipher = ""
    size = len(code)
    
    #go through each letter of the message
    for letter in message:
        if letter in code:              #make sure the character is in the alphabet
            x = code.index(letter)      #get number for letter from the code
            y = (a*x + b)%size          #calculate encryption value
            cipher += code[y]           #find the corresponding number in the code
        else:                           #if character isn't in alphabet
            cipher += letter            #add character to ciphertext 
    return cipher

def decode(message, a, b, code):
    plaintext = ""
    size = len(code)
    ainverse = inverse(a, size)         #get inverse of a
    for letter in message:
        if letter in code:              #make sure the character is in the alphabet
            y = code.index(letter)      #get number for letter from the code
            x = (ainverse *(y-b))%size  #calculate decryption value
            plaintext += code[x]        #add character to plaintext
        else:                           #if character isn't in alphabet
            plaintext += letter         #add character to plaintext
    return plaintext

def inverse(a, mod):
    num = 0
    while(((a*num)%mod)!=1):            #if it doesn't equal 1, it isn't an inverse
        num += 1
    return num                          #return inverse

def printable_table(code):
    paired = []
    for i in range(len(code)):
        temp = [code[i], i]             #create an array with letter and its index
        paired.append(temp)             #add it to a 2d array for printing
    return paired

def get_an_a(n):
    possiblea = []
    for i in range(n):
        if (math.gcd(i, n) == 1):       #find values where gcd(a, alphabet size) = 1
            possiblea.append(i)         #add them to a list
    print("Choose one of the following values to be a:\n{}".format(possiblea))
    choice = int(input("> "))
    while ((choice in possiblea) == False):
       print ("The a value must be one of the following values:\n{}".format(possiblea))
       choice = input("> ")
    return choice

if __name__ == "__main__":
    code = create_code()
    a = 1
    b = 1
    while True:
        print("\nAffine Cipher Encoder Decoder")
        print("---------------------")
        print("\tCurrent A Value: {}\n".format(a))
        print("\tCurrent B Value: {}\n".format(b))
        print("\t1. Print Affine Table.")
        print("\t2. Encode Message.")
        print("\t3. Decode Message.")
        print("\t4. Change B Value.")
        print("\t5. Change Cipher.")
        print("\t6. Change A Value.")
        print("\t7. Quit.\n")
        choice = input(">> ")
        print()
        
        if choice == '1':
            print("Table:")
            print(printable_table(code))
            
        elif choice == '2':
            message = input("\nMessage to encode: ")
            print("Encoded Message: {}".format(encode(message.upper(), a, b, code)))
            
        elif choice == '3':
            message = input("\nMessage to decode:")
            print("Decoded Message: {}".format(decode(message.upper(), a, b, code)))
        
        elif choice == '4':
            new_b = input("\nNew B value (currently{}): ".format(b))
            try:
                new_b = int(new_b)
                if new_b < 1 or new_b >len(code):
                    raise Exception("B value must be greater than 0 and less than the alphabet size")
            except ValueError:
                print("B value {} is not a valid number.".format(new_b))
            else:
                b = new_b
                code = create_code()
                
        elif choice == '5':
            code = create_code()
            print(printable_table(code))
            
        elif choice == '6':
            a = get_an_a(len(code))
            print ("New A value {}:".format(a))
            
        elif choice == '7':
            print("Terminating.\n")
            break
        
    else:
        print("Unknown option {}.".format(choice))
        