"""
add 3 numbers.ask numbers from user in a single line

45 67 44
"""

# n = input("enter numbers = ")
# b = n.split()
# print(b)
# for i in range(0, len(b)):
#     b[i] = int(b[i])
# print(b)

# n1, n2, n3 = b
# print(n1)
# print(n2)
# print(n3)


# n = input(" enter 3 numbers= ")
# print(list(map(int, n.split())))

a, b, c = list(map(int, input("enter 3 numbers").split()))
print(a, b, c)
