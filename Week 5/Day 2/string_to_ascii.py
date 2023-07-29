# s1 = input("enter a string : ")  # %
# print(ord(s1))  # 37


s1 = input("enter a string : ")  # aeroplane (sum of ascii values)
# print(sum([ord(i) for i in s1]))

sum = 0
for i in s1:
    sum = sum + ord(i)
print(sum)
