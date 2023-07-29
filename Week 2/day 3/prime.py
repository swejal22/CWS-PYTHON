"""
ask a number from user

check if the number is prime or not
"""
num = int(input("enter a number= "))
c = 0
for i in range(1, num + 1):
    if num % 1 == 0:
        print(i, end=" ")
        c = c + 1

print()
print(c)

if c == 2:
    print("it is a prime number")
else:
    print(" it is a composite number")
