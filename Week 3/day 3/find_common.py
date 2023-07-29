# find common elements in both list

a = [432, 546, 255, 444, 677, 986, 3456]
b = [4, 165, 255, 66, 8789, 6433, 90]

for i in a:
    if i in b:
        print(i, end=" ")
