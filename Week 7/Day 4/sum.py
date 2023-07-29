file = input("enter file name ")
N = int(input("enter n value = "))
with open("xyz.txt", "r") as file:
    r = file.readlines()
    if r == N:
        print(" n number of lines", N)
