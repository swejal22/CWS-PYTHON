a = [45, 3, 65, 45, 123, 65, 45, 321, 4, 654]
num = int(input("enter a number = "))

# if a.count(num) >= 1:
#     print("yes")
# else:
#     print("no")


# is/not is
# in/not in
if num in a:
    print("yes")
else:
    print("no")

if num not in a:
    print("it does not exist")
else:
    print("it exist")
