import random

a = ["sunny", "cloudy", "rainy", "snowy"]
b = int(input(" please enter number of days for the weather forecast = "))
for i in range(1, b + 1):
    x = random.choice(a)
    print(" day ", i, "=", x)
