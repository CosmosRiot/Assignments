#Countdown
def cdown(x):
    for i in range(x, -1, -1): 
        print(i)
cdown(5)

#Print and Return
def printReturn(a,b):
    print(a)
    return b
print(printReturn(10,400))

#First Plus Length
a = [2,2,3,4,5,6,1,1,1,1,1]
def firstLen(a):
    x = a[0]
    y = len(a)
    return x + y
print(firstLen(a))

#Values Greater than Second
y = [1,2,3,4,1,1,1]
def greater2nd(a):
    x = []
    for i in range(len(a)):
        if a[i] > a[1]:
            x.append(a[i])
    if len(x) < 2: 
        print("False")
    else:
        print(len(x))
        print(x)
greater2nd(y)

#This Length, That Value
def thisThat(a,b):
    x = []
    for i in range(a):
        x.append(b)
    return x
print(thisThat(20,100))