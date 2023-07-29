a = "aeroplane is a big transport"
# print(a[0])
# print(a[0:6])
# print(a[::-1])

# IMMUTABLE
# a[0] = "z"

# a = "good"
# a = 5
# print(a)

# print(f"length={len(a)}")
# for i in range(0, len(a)):
#     print(a[i], end=" ")

for i in range(len(a) - 1, -1, -1):
    print(a[i], end=" ")

for i in a:
    print(i, end="")
