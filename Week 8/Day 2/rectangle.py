# class rectangle:
#     length = int(input("enter the length"))
#     breadth = int(input("enter the breadth"))

#     def area(self):
#         self.area = self.length * self.breadth
#         print(f"area of rectangle is {self.area}")

#     def perimeter(self):
#         self.perimeter = 2 * (self.length + self.breadth)
#         print(f"pereimeter of rectangle is {self.perimeter}")


# a1 = rectangle()
# a1.area()
# a1.perimeter()


class Rectangle:
    def inputDimension(self):
        self.length = int(input("Enter length: "))
        self.breadth = int(input("Enter breadth: "))

    def area(self):
        return self.length * self.breadth

    def parameter(self):
        print(f"Parameter of rectangle is {2*(self.length + self.breadth)}")


a = Rectangle()


a.inputDimension()
area = a.area()
print(area)
