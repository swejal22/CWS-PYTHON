"""
print all the n umbers divisible by 5 from 1 to 100
"""
i = 1
while i <= 100:
    if i % 5 == 0:
        print(i, end=" ")
    i = i + 1
