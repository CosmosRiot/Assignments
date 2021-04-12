#Biggie Size
a = [1,-1,-500,3,98,-2,45,70]
def biggie(x):
    for i in range(0, len(x), 1):
        if x[i] > 0:
            x[i] = "big"
    return x
print(biggie(a))

#Count Positives
a = [-23, 1, 6, -8, 42, 3]
def countPos(x):
    count = 0
    for i in range(len(x)):
        if x[i] > 0: 
            count += 1
    x[len(x)-1] = count
    return x
print(countPos(a))

#Sum Total
a = [1,2,3,4,5]
def sumTotal(x):
    sum = 0
    for i in range(len(x)):
        sum += x[i]
    return sum
print(sumTotal(a))

#Average
a = [1,2,3,4]
def avg(x):
    sum = 0
    for i in range(len(x)):
        sum += x[i]
    average = sum / len(x)
    return average
print(avg(a))

# Length
a = [1,2,3,4,5,6]
def length(x):
    return len(x)
print(length(a))

#Minimum
a = [1,75,23,90,-4,2,645]
def min(x):
    if len(x) == 0:
        return "False"
    else:
        y = x[0]
        for i in range(1, len(x)):
            if x[i] < y:
                y = x[i]
        return y
print(min(a))

#Maximum
a = [1,75,23,93,-4,2,645]
def max(x):
    if len(x) == 0:
        return "False"
    else:
        y = x[0]
        for i in range(1, len(x)):
            if x[i] > y: 
                y = x[i]
        return y
print(max(a))

#Ultimate Analysis
ultimate = {
    "SumTotal" : "", 
    "Average" : "",
    "Minimum" : "", 
    "Maximum" : "",
    "Length" : "",
}

a = [1,2,3,4,5,6,7,8,9,10,11]
def ultilist(x):

    #SumTotal
    sum = 0
    for i in range(len(x)):
        sum += x[i]
    ultimate.update({"SumTotal" : sum})

    #Average
    avg = sum / len(x)
    ultimate.update({"Average" : avg})

    #Minimum
    min = x[0]
    for i in range(1, len(x)):
        if x[i] < min:
            min = x[i]
    ultimate.update({"Minimum" : min})

    #Maximum
    max = x[0]
    for i in range(1, len(x)):
        if x[i] > max: 
            max = x[i]
    ultimate.update({"Maximum" : max})

    #Length
    ultimate.update({"Length" : len(x)})

ultilist(a)
print(ultimate)

#Reverse List
a = [1,2,3,4,5,6,7,8,9,10]
def reverse(x):
    x.reverse()
    return x
print(reverse(a))