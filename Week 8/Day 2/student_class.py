class Student:
    def __init__(self):
        print("constructor is called")
        # def __init__(self, n, a, g):
        #         self.name = n
        #         self.age = a
        #         self.gender = g
        self.name = input("enter name =")
        self.age = int(input(" enter age ="))
        self.gender = input("enter gender = ")

    def greet(self):
        print(f"Your name is {self.name}")
        print(f"Your age is {self.age}")
        print(f"Your gender is {self.gender}")

    # def getData(self, n, a, g):
    #     self.name = n
    #     self.age = a
    #     self.gender = g


s1 = Student()
# s2 = Student()
# s1.getData("swejal", 23, "female")
print("--------")
s1.greet()
