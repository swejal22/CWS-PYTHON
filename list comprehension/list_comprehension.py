import datetime
import time

# t1 = datetime.datetime.now()
# # print("good")
# print(t1)
# time.sleep(2)
# # print("bye")
# t2 = datetime.datetime.now()
# print(t2)
# print(t2 - t1)

# print(datetime.datetime.now())

# a = []

t1 = datetime.datetime.now()
# for i in range(1, 500001):
#     a.append(i)
a = [i for i in range(1, 500001)]
t2 = datetime.datetime.now()

print(t2 - t1)

# print(a)
