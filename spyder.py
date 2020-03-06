print("Hello World!")
type(98)
str1="Cisco"
str2="Networking"
str3="Academy"
space=" "
print(str1+str2+str3)
hostnames=["R1","R2","R3","S1","S2"]
type(hostnames)
hostnames=["Motor","Frenos","Caja","Llantas","Embrague"]
type(hostnames)
hostnames

hostnames[-1]
hostnames[0]="Inyeccion"
hostnames

ipAddress= {"R1":"10.1.1.1","R2":"10.2.2.1","R3":"10.3.3.1"}
type(ipAddress)
ipAddress['R1']

ipAddress["S1"]="10.1.1.10"
ipAddress

"R3" in ipAddress 

x=input("Enter a number to count to: ")
x=int(x)
y=1
while y<=x:
    print(y)
    y=y+1
    if y>x:
        break

while True:
    x=input("Enter a number to count to: ")
    if x == "q" or x == "quit":
        break
    x=int(x)
    y=1
    
    while True:
        print(y)
        y=y+1
        if y>x:
            break

for i in range (5):
    print(i+1)
    
for i in range(1,n+1):
    result +=i
    
print(result)

for i in range(10,0,-2):
    print(i)