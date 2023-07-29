a = [54, 74, 85, 41, 52, 89, 41]
# b = []
# for i in range(0, len(a)):
#     if a[i] % 2 != 0:
#         b.append(a[i])
# print(b)

even = []
odd = []

for i in range(0, len(a)):
    if a[i] % 2 == 0:
        even.append(a[i])
    else:
        odd.append(a[i])
print(even)
print(odd)
