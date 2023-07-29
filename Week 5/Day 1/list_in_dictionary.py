# a = {
#     "sagar": [67, 74, 32, 12, 44],
#     "sanjay": [76, 32, 12, 34, 33],
#     "akul": [76, 88, 32, 4, 56],
# }

# print student name along with their total marks
# sagar has scored 333 marks

# for k, v in a.items():
#     print(f"{k} has scored {sum(v)}")

"""
sagar
67
74
32
12
44
"""
# for k, v in a.items():
#     print(k)
#     for i in v:
#         print(i)

"""
sagar 
44
12
32
74
67
"""
# for k, v in a.items():
#     print(k)
#     for i in v[::-1]:
#         print(i)

"""
sagar-> 74
sanjay -> 76
akul -> 88
"""
# for k, v in a.items():
#     print(f"{k} -> {max(v)}")

# 0R DIFF LOGIC

# for k, v in a.items():
#     max_marks = 0
#     for m in v:
#         if m > max_marks:
#             max_marks = m
#     print(f"name={k} and max marks = {max_marks}")

"""
overall maximum mark print 
"""

# max_marks = 0
# for k, v in a.items():
#     max_marks = 0
#     for m in v:
#         if m > max_marks:
#             max_marks = m

# print(max_marks)

# result = []
# for k, v in a.items():
#     result.extend(v)

# print(max(result))

a = {
    "sagar": [67, 74, 35, 12, 94],
    "sanjay": [78, 32, 2, 34, 33],
    "akul": [76, 88, 31, 4, 56],
}

"""
88 akul """

# result = []
# for k, v in a.items():
#     result.extend(v)

# max_marks = max(result)  # 94

# for k, v in a.items():
#     if max_marks in v:
#         print(k, max_marks)

a = {"a": 5, "e": 2, "c": 10, "d": 1, "b": 2}
b = {}
c = sorted(list(a.values()))

print(c)

for i in c:
    for k, v in a.items():
        if v == i:
            b.update({k: v})

print(b)
