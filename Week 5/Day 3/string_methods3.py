# a = "Aeroplane is better transport"
# b = a.replace("e", "z")
# print(b)

# user_string = input("enter sentence = ")
# letter = input("enter a letter = ")

# if user_string.find(letter) == -1:
#     print("does not exist")
# else:
#     print(" it exist")

# if user_string.count(letter) == 0:
#     print("does not exist")
# else:
#     print(" it exist")


# user_string = input("Enter a sentence = ")

# isLetter = False
# isNumber = False

# for i in user_string:
#     if i.isdigit():
#         isNumber = True
#     elif i.isalpha():
#         isLetter = True

# if isNumber == True and isLetter == True:
#     print("Both number and letter exists")
# else:
#     print("Both number and letter does not exists")

"""
ask sentence
ask letter
if letter exists 
then only ask new letter
then replace old letter with new letter

else 
print does not exists
"""
user_string = input("Enter a sentence = ")
letter = input("Enter a letter = ")

if letter in user_string:
    new_letter = input("Enter new letter = ")
    result = user_string.replace(letter, new_letter)
    print(result)
else:
    print("Does not exists")
