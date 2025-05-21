#         012345678901234
parrot = "Norwegian Blue"
print()

print(parrot[0:6:2])
print(parrot[0:6:3])

number = "9,223,372,036,854,775,807"
print(number[1::4])

number = "9,223;37:036 854,775;807"
print(number[1::4])
seperators = number[1::4]
print(seperators)