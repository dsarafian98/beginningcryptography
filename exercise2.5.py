# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 13:55:45 2020

@author: Danielle
"""

import hashlib
import timeit
import random
import string


def function():
    start = timeit.default_timer()
    for numTimes in range (10):
        alphabet = string.ascii_lowercase
        num = random.randint(0, len(alphabet))
        randLetter = alphabet[num]
        encoded = randLetter.encode()
        print(encoded)
        print(randLetter)
        
        m = hashlib.md5()
        m.update(encoded)
        testHash = m.hexdigest()
        print(testHash)
        
        match = False
        i =  0
        while (match != True and i < len(alphabet)):    
            alphabetLetter = alphabet[i].encode()
            theNewOne = hashlib.md5()     
            theNewOne.update(alphabetLetter)
            thisHash = theNewOne.hexdigest()
            print(thisHash)
            match = (thisHash == testHash)
            i+=1
        print ("We found a match!")
        print("random letter: {}\nwe found: {}".format(randLetter, alphabetLetter))
    end = timeit.default_timer()
    print("time taken: {}".format(end - start))
function()