"""
ask a number and print factors of that number
16->1,2,4,8,16
10-> 1,2,5,10
25-> 1,5,25


count the n umber of factors

count factors as well as number :
"""
# a = int(input("enter a number = "))
# factor = 1
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")


# a = int(input("enter a number = "))
# factor = 1
# for i in range(1, a):
#     if a % i == 0:
#         factor = factor + 1
# print(factor)

num = int(input("enter a number= "))
c = 0
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
        c = c + 1
print()
print(c)
