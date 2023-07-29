"""

"""
a = {"physics": 69, "chemistry": 95, "maths": 18, "english": 80, "cs": 89}
# a={"physics":74,"chemistry":100,"maths":23,"english":85,"cs":94}

b = {}
# for k, v in a.items():
#     b[k] = v + 5
# print(b)

for k, v in a.items():
    if v > 33:
        b[k] = "pass"
    else:
        b[k] = "fail"
print(b)
