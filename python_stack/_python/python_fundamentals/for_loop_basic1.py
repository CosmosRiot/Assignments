#Basics
# for x in range(151): 
#     print(x)

#Multiples of Five
# for i in range(5, 1005, 5):
#     print(i)

#Counting, the Dojo Way
# for i in range(1, 101): 
#     if i % 10 == 0: 
#         print("Coding Dojo")
#     elif i % 5 == 0: 
#         print("Coding")
#     else: 
#         print(i)

#Whoa, That Sucker's Huge
# x = 0
# for i in range(500001): 
#     if i % 2 == 1: 
#         x += i
# print(x)

#Countdown by Fours
# for i in range(2018, 0, -4): 
#     print(i)

#Flexible Counter
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum + 1):
    if i % mult == 0: 
        print(i)
