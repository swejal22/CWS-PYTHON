a = [45, 3, 65, 45, 123, 65, 45, 321, 4, 654]
b = []

for i in a:
    if i not in b:
        b.append(i)
print(b)

# count the number of frequency of each number
for i in b:
    count = a.count(i)
    print(f"{i} occurs {count} times")


# odd even

# a = [45, 3, 65, 45, 123, 65, 45, 321, 4, 654]
# even = []
# odd = []
# for i in a:
#     if i % 2 == 0:
#         even.append(i)
# print(even)
# for i in a:
#     if i % 2 != 00:
#         odd.append(i)
# print(odd)
