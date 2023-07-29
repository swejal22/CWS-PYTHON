a = " swejal is good girl"
b = list(a)
print(b)

# a = ["swejal", " is", " good", " girl"]
# b = " ".join(i for i in a)
a = [52, 45, 3222, 567, 778, 7]
b = " |".join(str(i + 5) for i in a)
print(b)
print(type(b))
