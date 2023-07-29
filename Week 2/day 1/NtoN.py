"""
1.ask two numbers from user ->start,end
2.print numbers divisible by 5
"""
start = int(input("enter start number= "))
end = int(input("enter end number= "))

# i = start
# while i <= end:
#     print(i, end=" ")
#     i = i + 1

i = start
while i <= end:
    if i % 5 == 0:
        print(i, end=" ")
    i = i + 1
