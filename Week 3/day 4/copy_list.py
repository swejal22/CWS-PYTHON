a = [43, 32, 154, 654, 76, 78687, 32]  # 500
b = a.copy()
print(id(a))
print(id(b))

print(a)
print(b)

# a=[99,33] #300
a[3] = 1000
print(a)
print(b)
