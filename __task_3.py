textInput = input("Enter some text: ")
textInput.count("T")
# d = dict()

d = {i: textInput.count(i) for i in textInput if not i.isspace()}

# for i in textInput:
#     print(i, textInput.count(i))
#     if i in d:
#         continue
#     else:
#         d[i] = textInput.count(i)

print(d)
