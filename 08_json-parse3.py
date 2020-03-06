# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 19:58:19 2020

@author: CEC
"""

while True:
    orig=input("Starting Location:")
    dest=input("Destination:")
    url=main_api + urllib.parse.urlencode({"key":key,"from":orig,"to":dest})
    print("URL:"+(url))
    