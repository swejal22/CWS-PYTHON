# tuple vs list
"""
list is mutable
tuple is immutable

"""
a = (45, 32, 12, 3, 33)
print(a)
print(type(a))

# a[0]=100
# print(a)

r = a.count(100)  # occurence
print(r)

r = a.index(32)
print(r)

for i in a:
    print(i, end=" ")
