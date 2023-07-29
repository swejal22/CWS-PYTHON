"""
only list and dictionary change from inside """


def xyz(a):
    a["aaa"] = "bbbb"


x = {"swejal": 99, "nikhil": 100}
print(f"dictionary before calling function(outside)={x}")
xyz(x)
print(f"dictionary after calling function (outside)={x}")


def pqr(s):
    s = s.replace("a", "z")
    print(f"inside function{s}")


a = "swejal"
