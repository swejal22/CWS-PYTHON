# [1,0,1,0,1,0,1,0,1,0]
# [odd,even,odd,even,odd]

# a = [i for i in range(1, 101)]
# print(a)

a = [i for i in range(1, 11) if i % 2 == 0]
print(a)

# a = [f"even - {i}" if i % 2 == 0 else f"odd - {i}" for i in range(1, 11)]
# print(a)

# print(
#     sum(
#         [
#             i
#             for i in range(
#                 int(input("enter start number = ")),
#                 int(input("enter end number = ")) + 1,
#             )
#         ]
#     )
# )
