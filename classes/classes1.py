class Abc:
    def setChild(self, childObj):
        # self.child=obj (which is part of XYZ)
        self.child = childObj

    def display(self):
        self.child.displayChild()


class Xyz:
    def displayChild(self):
        print("I am a display")


obj = Xyz()
obj1 = Abc()
obj1.setChild(obj)
obj1.display()
