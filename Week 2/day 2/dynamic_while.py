"""
enter start number =54
enter end number =23
"""
start = int(input("enter start number=  "))
end = int(input("enter end number=  "))
i = start
while i >= end:
    print(i, end=" ")
    i = i - 1
