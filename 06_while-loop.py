# -*- coding: utf-8 -*-

#While Loop
x=input("Enter a number to count to: ")
x=int(x)
y=1
while y<=x:
    print(y)
    y=y+1
  
#While Loop to Use Break
x=input("Enter a number to count to: ")
x=int(x)
y=1
while y<=x:
    print(y)
    y=y+1
    if y>x:
        break

# While Loop to Check for User Quit
while True:
    x=input("Enter a number to count to: ")
    if x == 'q' or x == 'quit':
        break 
x=int(x)
y=1
while True:
    print(y)
    y=y+1
    if y>x:
        break