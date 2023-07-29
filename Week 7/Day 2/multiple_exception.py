# try:
#     a = [54, 32, 21, 32, 43, 0]
#     print(a[4])
#     # print(a[0] / a[-1])
#     # print(b)
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except IndexError:
#     print("wrong index given")

# except:
#     print("some error occured")

try:
    a = int(input("Enter number 1 = "))
    b = int(input("Enter number 2 = "))
    c = int(input("Enter number 3 = "))
    print(a + b + c)

except ValueError:
    print("please enter proper integer")
