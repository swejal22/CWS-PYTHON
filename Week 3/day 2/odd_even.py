a = [41, 74, 85, 41, 52, 89]
even = []
odd = []

for i in range(0, len(a)):
    if a[i] % 2 == 0:
        even.append(a[i])
    else:
        odd.append(a[i])

# print(even)
# print(odd)

print(f"number of even number = {len(even)}")
print(f"number of odd number = {len(odd)}")
