"""
2 function
sumlist,check 

sumlist(a)->return sum

then check odd or even
"""


def sumlist(customlist):
    total = sum(customlist)
    return total


def check(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd")


x = [10, 30, 10]

r = sumlist(x)
print(r)
check(r)
