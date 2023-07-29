a = [43, 756, 24, 654, 5687, 2, 4, 567, 87, 42]
# print(a[2:5])

for i in a[3:7]:
    print(i, end=" ")

b = a[2:5]
print(b)

print(a[4 : len(a)])  # a[4:10]
print(a[0:1])
print(a[0:10:3])
print(a[2:])
print(a[0:])
print(a[2:-1])
print(a[6:-2])
print(a[-1:-6:-1])
print(a[-1::-1])
print(a[5:0:-2])
