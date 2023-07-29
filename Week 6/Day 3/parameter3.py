def marks(phy: int, chem: int, eng: int, sst: int):
    print(f"total is {phy+chem+eng+sst}")
    p = (phy + chem + eng + sst) * 100 / 400
    print(f"percentage is {p}")


marks(20, 45, 65, 99)
