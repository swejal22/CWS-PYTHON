"""
ask a number from user =
54653
count the number of digits=5

122111
count the number of digits =6
// (hint)
"""
"""
4534 ->  4534//10  -> 453
453 -> 453//10 -> 45
45 -> 45//10 -> 4
4 -> 4//10 -> 0
"""
n = 1589658745
count = 0
while n > 0:
    count = count + 1
    n = n // 10

print(count)
