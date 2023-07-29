def greet(name):
    print(f"greetings to {name}")
    pass


def add(a, b, c):  # -->parameter
    print(a + b + c)


def marks(phy, chem, eng, sst):
    print(f"total is {phy+chem+eng+sst}")
    p = (phy + chem + eng + sst) * 100 / 400
    print(f"percentage is {p}")


greet("swejal")  # --> argument
add(20, 20, 10)
marks(30, 20, 40, 30)
