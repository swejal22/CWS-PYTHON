# a = {"name": "swejal", "age": 23, "gender": "female"}
a = {"physics": 44, "chem": 66, "history": 100}

# for i in a.keys():
#     print(i)

# for i in a.keys():
#     print(a[i])


# calculate total of all the values
# total = 0
# for i in a.values():
#     total = total + i
# print(total)


"""
marks in physics is 44
marks in chem is 66
marks in history is 100
"""

# print(a.items())
for k, v in a.items():
    print(k, v)  # print(f"marks in {k} is {a[k]}")

# for k in a.keys():
#     print(f"marks in {k} is {a[k]}")
