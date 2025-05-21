name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

# if age >= 18:
#     print("{0} is old enough to vote.".format(name))
#     print("Please put an X in the box")
# else:
#     print("{0} is NOT old enough to vote. Please come back in {1} years.".format(name, (18 - age)))


print()

if age < 18:
    print("{0} is NOT old enough to vote. Please come back in {1} years.".format(name, (18 - age)))
elif age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi")
else:
    print("You are old enough to vote.")
    print("Please put an x on the box")
