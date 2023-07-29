"""
n-> enter a number #45

[1,3,5,.....45]
"""
# n = int(input("enter a number = "))
# print([i for i in range(1, n + 1) if n % i == 0])


n = int(input("enter a number = "))
factors = [i for i in range(1, n + 1) if n % i == 0]

print("prime" if len(factors) == 2 else " not prime")
# n = 3
# print("even" if n % 2 == 0 else "odd")
