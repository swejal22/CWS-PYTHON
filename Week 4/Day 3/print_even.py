"""
put 5 subject name and marks in a dictionary.
printthe totalof all marks divisible by 2
"""

a = {"physics": 56, "chem": 50, "maths": 67, "bio": 90, "eng": 77}
total = 0

for m in a.values():
    if m % 2 == 0:
        total = total + m
print(total)
