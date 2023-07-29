a = [45, 3, 65, 45, 123, 65, 45, 321, 4, 654]
maximum = a[0]
for i in range(1, len(a)):
    if a[i] > maximum:
        maximum = a[i]
print(maximum)
