"""
count the numbers divisible by 11 from 1 to 100
9
"""
i = 1
count = 0
while i <= 100:
    if i % 11 == 0:
        count = count + 1
    i = i + 1
print(count, end=" ")
