"""

printnumber()
start =44
end=66
44 to 66-> sum
"""


def printnumber():
    a = int(input(" enter a number = "))
    b = int(input(" enter a number = "))
    total = 0
    for i in range(a, b + 1):
        total = total + i
    print(total)


printnumber()
