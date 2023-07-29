"""
ask a number from user
enter a number =7
print 1 to N 

divisible by 8. print those number
1-100 -> count numbers

sum of those numbers
"""
# a = int(input("enter a number = "))
# for i in range(1, a + 1):
#     print(i, end=" ")


# a = int(input("enter a number = "))
# for i in range(1, a + 1):
#     if i % 8 == 0:
#         print(i, end=" ")


# a = int(input("enter a number = "))
# count = 0
# for i in range(1, a + 1):
#     if i % 8 == 0:
#         count = count + 1
# print(count)


a = int(input("enter a number = "))
count = 0
sum = 0
for i in range(1, a + 1):
    if i % 8 == 0:
        count = count + 1
        sum = sum + i
print(sum)
