# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 19:22:26 2020

@author: CEC
"""
def isPrime(num):
    #Función que determina si un número es primo
    if num<2: 
        return False
    elif num==2:
        return True
    else:
        for in range (1,20):
            if isPrime(i+1):
                print(i+1,end=" ")
    print()

def isPrime(n):
    #Función que determina si un número es primo
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            return False
        