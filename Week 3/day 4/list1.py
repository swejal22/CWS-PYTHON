"""
list in python
a=[43]
"""

a = [43, 67, 11, "swejal", "22.22", 22.2, True]
print(a)
print(type(a))

a = [42, 46, 78, 98, 90, 65, 44]
for abc in range(0, len(a), 1):
    print(a[abc])

# reverse print
a = [42, 46, 78, 98, 90, 65, 44]
for abc in range(len(a) - 1, -1, -1):  # or (-1,-(len(a)+1),-1)
    print(a[abc])
