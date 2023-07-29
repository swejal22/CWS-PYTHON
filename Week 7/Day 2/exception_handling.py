"""
exception handling
"""
try:
    a = int(input("enter number 1 = "))
    b = int(input("enter number 2 = "))
    print(a / b)

except:
    print("some error occured")

else:
    print("this is else statement")
finally:
    print("this is a final statement")
