a = {"name": "swejal", "age": 23, "gender": "female"}

# a["name"]="pankaj"
# a.update({"name": "pankaj", "physics": 54})


# del a["name"]

# ask key from user,if key exists,then delete that key

# for i in a:
#     print(i)

keyname = input("enter key you want to delete = ")
# if a.get(keyname) != None:
if keyname in a:
    a.pop(keyname)
    print(a)
else:
    print("key does not exist")


# a.pop("name")
# print(a)
