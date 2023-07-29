# a = {}
# for i in range(0, 5):
#     sub = input("enter subject name= ")
#     marks = int(input("enter marks= "))
#     a[sub] = marks
# print(a)

a = {}

name = input("enter  name= ")
a["name"] = name
age = int(input("enter age= "))
a["age"] = age
gender = input("enter gender = ")
a["gender"] = gender

for i in range(0, 5):
    sub = input("enter subject name= ")
    marks = int(input("enter marks= "))
    a[sub] = marks
print(a)
