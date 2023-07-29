"""
classes and object
class is bluprint
"""


class student:
    # data members/attribute
    name = " "
    age = 0
    gender = " "

    # methods
    def greet(self):
        print("this is a greet method")
        print(f"your name is {self.name}")
        print(f"your age is {self.age}")
        print(f"your gender is {self.gender}")
        # print(self.city)

    def getdata(self):
        self.name = input("enter name =")
        self.age = int(input(" enter age ="))
        self.gender = input("enter gender = ")
        # self.city = "pune"


s1 = student()
s2 = student()
s3 = student()
s1.getdata()
s1.greet()
print("------")
s2.getdata()
s2.greet()
print("-------")
s3.greet()
# s2.greet()
# s1.name = "swejal"
# s1.age = 23
# s1.gender = "female"
# s1.greet()
# s2.name = "nikhil"
# s2.age = 26
# s2.gender = "male"
# print(s1.name)
# print(s1.age)
# print(s1.gender)
# print(s2.name, s2.age, s2.gender)
