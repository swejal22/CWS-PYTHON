"""
enter start number =1
enter end number=30
7+14+21+28

calculate sum of all the number divisible by 7
from start to end
"""
start = int(input("enter start number = "))
end = int(input("enter end number = "))
total = 0
while start <= end:
    if start % 7 == 0:
        total = total + start
    start = start + 1
print(total)
