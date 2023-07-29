"""
abc.txt

number of lines =10
"""
f = open("abc.txt", "r")
r = f.readlines()
print(len(r))
print(r)
