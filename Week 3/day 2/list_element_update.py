# update element at a position

a = [24, 56, 78, 89, 00, 12, 44]
print(a)

a[0] = 100
a[-1] = 100
print(a)

# a[0] = a[0] + 5
# a[1] = a[1] + 5
# a[2] = a[2] + 5
# a[3] = a[3] + 5
# a[4] = a[4] + 5

for i in range(0, len(a)):
    a[i] = a[i] + 5

print(a)

# add 5 in even number and -5 in odd numbers


for i in range(0, len(a)):
    if a[i] % 2 == 0:
        a[i] = a[i] + 5
    else:
        a[i] = a[i] - 5
print(a)

# do 0 at the place of even number
for i in range(0, len(a)):
    if a[i] % 2 == 0:
        a[i] = 0

print(a)
