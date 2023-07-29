"""
4 type function :
without parameter , without return
with parameter , without return
without parameter , with return
with parameter , with return
"""


def addition(a, b):
    total = a + b
    return total


x = addition(10, 20)
print(x)


def addition(a, b, c):
    total = a + b + c
    return total


# print(addition(10, 20, 30))
x = addition(10, 20, 30)
print(x)
