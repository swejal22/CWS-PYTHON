# a = []
# for i in range(0, 5):
#     num = int(input("enter a number = "))
#     a.append(num)

# print(a)


# a = []
# n = int(input(" how many elements = "))
# for _ in range(0, n):
#     num = int(input("enter a number = "))
#     a.append(num)

# print(a)

# add 5 elements
# 55
# 23
# 43
# 65
# 76
# [76,65,43,23,55]


# a = []
# n = int(input(" how many elements = "))
# for _ in range(0, n):
#     num = int(input("enter a number = "))
#     a.insert(0, num)

# print(a)

# count 55

count = 0
a = [10, 54, 78, 74, 85, 74, 84, 114, 44, 55, 55, 55, 55]
for i in range(0, len(a)):
    if a[i] == 55:
        count = count + 1
print(count)
