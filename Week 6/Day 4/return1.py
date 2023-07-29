"""
write a function which returns addition of two values
check if sum is odd or even
addition ,check

"""


def addition(n1, n2):
    return n1 + n2


def check(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd")


x = addition(10, 20)

check(x)
check(100)
