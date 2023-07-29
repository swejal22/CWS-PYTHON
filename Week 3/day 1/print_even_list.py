"""

print all even numbers in a list
"""

a = [23, 12, 45, 64, 78, 67]

# for i in range(0, len(a)):
#     if a[i] % 2 == 0:
#         print(a[i])

for i in range(0, len(a)):
    if a[i] % 3 and a[i] % 4 == 0:
        print(a[i])

# print sum of even numbers :

a = [54, 67, 88, 34, 56, 79, 70]
total = 0
for i in range(0, len(a), 1):
    if a[i] % 2 == 0:
        total = total + a[i]
print(f"total is {total}")
