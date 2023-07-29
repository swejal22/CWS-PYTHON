# user_string = "aeroplane is a good mode of transport"
# # transport of mode good a is aeroplane

# b = user_string.split()
# print(b)
# b.reverse()  # b=b[::-1]
# print(b)
# print(" ".join(i for i in b))


# user_string = "aeroplane is a good mode of transport good bye ok done"
# words = user_string.split()
# print(words)

# # for i in range(0,len(words,2)):
# #     print(words[i],ends=" ")

# for i in words[::2]:
#     print(i, end=" ")


user_string = "aeroplane is a good mode of transport good bye ok done"
# words = user_string.split()[::2]
# print(words)
# print(" ".join(i for i in words))


# words = user_string.split()
# print(words)
# r = set(words)
# print(r)
# s = list(r)
# print(s)


# result = []
# for i in user_string.split():
#     if i not in result:
#         result.append(i)
# print(result)


user_string = "aeroplane is a good mode of transport good bye ok done"
# enalporea ko si a doog edom fo a tropsnart doog eyb ko enod

for i in user_string.split():
    print(i, end=" ")
    # print(i[::-1], end=" ")

print(" ".join(w[::-1] for w in user_string.split()))

# enod ko eyb tropsnart a fo edom doog a si ko enalporea
for i in user_string.split()[::-1]:
    print(i[::-1], end=" ")
