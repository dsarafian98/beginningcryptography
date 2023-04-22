# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 13:30:23 2020

@author: Danielle and Fabien
"""
import math

# NEVER USE: ECB is not secure!
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Alice and Bob's Shared Key
test_key = bytes.fromhex('00112233445566778899AABBCCDDEEFF')

aesCipher = Cipher(algorithms.AES(test_key),
                   modes.ECB(),
                   backend=default_backend())
aesEncryptor = aesCipher.encryptor()
aesDecryptor = aesCipher.decryptor()

message = b"""
FROM: FIELD AGENT ALICE
TO: FIELD AGENT BOB
RE: Meeting
DATE: 2001-1-1

Meet me today at the town square at 2300."""

message += b"E" * (-len(message) % 16)
ciphertext = aesEncryptor.update(message)

print("plaintext:",message)
print("ciphertext:",ciphertext.hex())

length = len(ciphertext.hex())
x = math.floor(length/32)
start = 0
end = 32
for i in range(x):
    print("block {}:".format(i), ciphertext.hex()[start:end])
    start = end
    end +=32  
"""recovered = aesDecryptor.update(ciphertext)
print("recovered:",recovered)
if(message==recovered): print("[PASS]")
else: print("[FAIL]")"""

print("\nNEW MESSAGE\n")

message2 = b"""
FROM: FIELD AGENT ALICE
TO: FIELD AGENT BOB
RE: Meeting
DATE: 2001-1-2

Meet me today at the town square at 1130."""

message2 += b"E" * (-len(message2) % 16)
ciphertext2 = aesEncryptor.update(message2)

print("plaintext:",message2)
print("ciphertext:",ciphertext2.hex())

length2 = len(ciphertext2.hex())
y = math.floor(length2/32)
start = 0
end = 32
for i in range(y):
    print("block {}:".format(i), ciphertext2.hex()[start:end])
    start = end
    end +=32
    
    
blockToSwitch = int(input("Which blocks would you like to switch?\n"))
startIndex = int(blockToSwitch*32)
endIndex = int(startIndex+32)
#s = slice(startIndex, endIndex)
print(startIndex)

array = bytearray(ciphertext)
array2 = bytearray(ciphertext2)

#print("{}\n".format(ciphertext[startIndex:endIndex].hex()))
#print("{}\n".format(ciphertext2[startIndex:endIndex].hex()))
#print("{}\n".format(ciphertext[endIndex:].hex()))
modMessage = array[:int(startIndex)] + array2[int(startIndex):int(endIndex)] + array[int(endIndex):]
print("It works when you hard-code a number")
print(array2[:32].hex())
print("but not when you use a variable")
print(array2[int(startIndex):int(endIndex)])
modMessage2 = array2[:int(startIndex)] + array[int(startIndex):int(endIndex)] + array2[int(endIndex):] 


"""newMessage1 = aesDecryptor.update(modMessage)
print("New message 1:",newMessage1)

newMessage2 = aesDecryptor.update(modMessage2)
print("New message 2: ", newMessage2)"""

print("Switched blocks: \n")
print(modMessage.hex()[int(startIndex):int(endIndex)])
print(modMessage2.hex()[int(startIndex):int(endIndex)])

"""start = 0
end = 32
for i in range(x):
    print("block {}:".format(i), modMessage.hex()[start:end])
    print("block {}:".format(i), modMessage2.hex()[start:end])
    start = end
    end +=32 """


