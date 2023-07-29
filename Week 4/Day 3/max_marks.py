"""
find maxmimum marks in a dictionary
the maximum mraks is 90 of bio
"""
a = {"physics": 56, "chem": 50, "maths": 67, "bio": 90, "eng": 77}
# marks = []

# for v in a.values():
#     marks.append(v)

# print(max(marks))

# print(max(a.values()))


# max_marks = 0
# for v in a.values():
#     if v > max_marks:
#         max_marks = v
# print(max_marks)


max_marks = 0
max_marks_subject_name = ""

for k, v in a.items():
    if v > max_marks:
        max_marks = v
        max_marks_subject_name = k

print(max_marks_subject_name)
print(max_marks)
