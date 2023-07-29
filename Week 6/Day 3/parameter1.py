# calculate sum of both lists
def sumoflist(a, b):
    # sum = a + b
    # print([sum])
    print(sum(a) + sum(b))


def marks(phy, chem, eng, sst):
    print(f"total is {phy+chem+eng+sst}")
    p = (phy + chem + eng + sst) * 100 / 400
    print(f"percentage is {p}")


# named parameters
marks(sst=99, chem=87, phy=45, eng=78)


# sumoflist([20, 35, 67, 33, 2, 60], [45, 88, 94])
sumoflist(a=[10, 20, 30], b=[45, 68, 43, 2])
