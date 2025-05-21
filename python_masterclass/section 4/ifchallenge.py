name = input("What is your name? ")
age = int(input("What is your age? "))

if 18 <= age < 31:
    print("You can go on a holiday {}".format(name))
else:
    print("Sorry {}, but you cannot go on holiday".format(name))