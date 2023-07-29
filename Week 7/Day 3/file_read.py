"""

3 types of mode to open a file :
   1.read
   2.write
   3.append
"""


f = open("abc.txt", "r")
# r = f.read()
# print(r)

# a = f.readline()
# print(a)

b = f.readlines()
print(b)
f.close()
