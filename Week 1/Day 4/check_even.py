"""
ask a number from user

if the number is divisible by 5 and 6 -> print yes else no"""

num = int(input("number is "))
if num % 5 == 0 and num % 6 == 0:
    print("yes")
else:
    print("no")
