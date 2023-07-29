"""
enter number=5
enter power=3
(5*5*5)
result=125

enter a number =2
enter power =8
2*2*2*2*2*2*2*2

result = 256
"""
num = int(input("enter a number = "))
power = int(input("enter a power = "))
i = 1
result = 1
while i <= power:
    result = result * num
    i = i + 1
print(result)
