"""
enter start number =1
enter end number =100
30 60 90
 1 to 100 ..... print all number divisble by 5 and 6
 """

start = int(input("enter start number=  "))
end = int(input("enter end number=  "))
if start <= end:
    while start <= end:
        if start % 5 == 0 and start % 6 == 0:
            print(start, end=" ")
        start = start + 1
else:
    while start >= end:
        if start % 5 == 0 and start % 6 == 0:
            print(start, end=" ")
        start = start - 1
