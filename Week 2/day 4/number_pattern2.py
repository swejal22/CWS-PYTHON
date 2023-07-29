"""
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1 

5
4 4
3 3 3 
2 2 2 2
1 1 1 1 1 

5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
"""
# for i in range(1, 6):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()

# for i in range(5, 0, -1):
#     for j in range(6, i, -1):
#         print(i, end=" ")
#     print()


for i in range(5, 0, -1):
    for j in range(5, i - 1, -1):
        print(j, end=" ")
    print()
