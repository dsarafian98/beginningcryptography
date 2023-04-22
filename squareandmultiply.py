# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 18:00:22 2020

@author: Danielle
"""

import sys

a=3
b=76
mod = 77

def exp_func(x, y, mod):
    exp = bin(y)
    print ("Binary value of b is:{}",exp)
    print ("Bit\tResult")
    value = x
 
    for i in range(3, len(exp)):
        value = value * value
        value = value%mod
        print (i-1,":\t",value,"(square)")
        if(exp[i:i+1]=='1'):
            value = value*x
            value = value%mod
            print (i-1,":\t",value,"(multiply)")
    return value

print ("We will calculate a^b")
print ("a=",a)
print ("b=",b)
print ("==== Calculation ====")
res=exp_func(a,b,mod)
print ("Result:",res)

print ("===========")