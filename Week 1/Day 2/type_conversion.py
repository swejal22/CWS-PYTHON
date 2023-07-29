"""
type coversion/type casting
convert one data type to another
"""
a = 44
print(type(a))
b = str(a)
print(type(b))

c = "456"
d = int(c)
print(d, type(d))

a = 345
b = bool(a)
print(b, type(b))

a = " "
b = bool(a)
print(b, type(b))
