# a = "        aeroplane is a vehicle      "
# # b = a.strip()
# b = a.lstrip()
# b = a.rstrip()
# print(a)
# print(b)

# a = "        aeroplane is a vehicle   @@@"
# b = a.strip("@")
# print(a)
# print(b)

# a = "shhguhdjsji"
# b = a.count("j")
# print(b)

a = "shhguhdjsji"
b = a.find("j")  # defines position #if letter doesnt exkist then -1
print(b)

a = "shhguhdjsji"
b = a.index("j")  # if doesnt exist then shows error
print(b)
