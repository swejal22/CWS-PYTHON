"""
print total of all the numbers divisible by 5
from 1 to 100 using list comprehension"""


print(sum([i for i in range(1, 101) if i % 5 == 0]))
print(len([i for i in range(1, 101) if i % 5 == 0]))
