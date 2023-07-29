"""
ask 5 subject marks from user
phy,chem,comp,eng,history (out of 100)
calculate percentage
percentage > 33 : pass
else fail
"""
phy = int(input("enter phy marks ="))
chem = int(input("enter chem marks ="))
comp = int(input("enter comp marks ="))
eng = int(input("enter eng marks ="))
history = int(input("enter history marks ="))
sum = phy + chem + comp + eng + history
print(sum)
percentage = (sum / 500) * 100
print(percentage)
if percentage > 33:
    print("pass")
else:
    print("fail")
