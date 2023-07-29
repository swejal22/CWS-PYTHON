a = [233, 2222, 45, 34, 65, 77, 6678, 789, 789, 897, 65, 33]

"""
enter start index=2
enter end index = 5
"""
start = int(input(" enter start index ="))
end = int(input("enter end inex = "))
for i in range(start, end + 1):
    print(a[i], end=" ")
