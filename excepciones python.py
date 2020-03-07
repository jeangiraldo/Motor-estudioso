# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 12:49:17 2020

@author: CEC
"""

try:
    print("1")
    x=1/0
    print("2")
except:
    print("Oh dear, something went wrong...")
    
print("3")

try:
    x=int(input("Enter a number"))
    y=1/x
    print(y)
except ZeroDivisionError:
    print("You must enter an integer value.")
except:
    print("oh dear, something went wrong...")
print("THE END.")

