# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:28:45 2020

@author: CEC
"""

def reciproco(n):
    try:
        n=1/n
    except ZeroDivisionError:
        print("División fallida")
        return None
    else:
        print("Todo salió bien")
    finally:
        print("Es el momento de decir adiós")
        return n
    
print(reciproco(2))
print(reciproco(5))