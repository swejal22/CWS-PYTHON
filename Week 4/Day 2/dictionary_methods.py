a = {"name": "swejal", "age": 23, "gender": "female"}

# print(a)
# a.clear()

keyname = input("enter key name= ")
if a.get(keyname) != None:
    print(a[keyname])
else:
    print("key does not exist")

# r = a.get("name")
# print(r)
# # a=None
# print(a)
# print(type(a))
