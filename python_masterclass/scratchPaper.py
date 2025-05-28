# Section 3:17
# Our first python program


# print('Hello, World!')


# Section 3:18
# Printing in Python

# print('Hello, World!')
# print (1 + 2)
# print (7 * 6)
# print()
# print("The end", "or is it?", "keep watching to learn more about Python", 3)

# Section 3:19
# Strings in Python
# print()

# print("Today is a good day to elarn Python")
# print('Python is fun')
# print("Python's string are easy to use")
# print('We can even include "quotes" in strings')
# print("Hello" + " world")
# print()

# greeting = "Hello"
# name = "Bruce"

# # if we want a space, we can add that too
# print(greeting + " " + name)
# print()

# # Get input from keyboard by using input
# name = input("Please enter your name: ")
# print(greeting + " " + name)

# Section 3:20
# The escape character
# print()
# print("next line")
# splitString = "This string has been\nsplit over\nseveral\nlines"
# print(splitString)
# print()

# print("Tabbed")
# tabbedString = "1\t2\t3\t4\t5"
# print(tabbedString)
# print()

# print('the pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')

# # OR

# print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")

# print("""The pet shop owner said "No, no, 'e's uh,...he's resting".""")

# print()

# anotherSplitString = """This string has been \
# split over \
# several \
# lines"""
# print(anotherSplitString)
# print()

# Section 3:21
# More on Escape Characters in String

# print()
# print("next line")
# splitString = "This string has been\nsplit over\nseveral\nlines"
# print(splitString)
# print()

# print("Tabbed")
# tabbedString = "1\t2\t3\t4\t5"
# print(tabbedString)
# print()

# print('the pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')

# # OR

# print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")

# print("""The pet shop owner said "No, no, 'e's uh,...he's resting".""")

# print()

# anotherSplitString = """This string has been \
# split over \
# several \
# lines"""
# print(anotherSplitString)
# print()

# print("C:\\Users\\ahernandez\\notes.txt")
# print(r"C:\Users\ahernandez\notes.txt")
# print()

# Section 3:22
# Variables and Types

# print()
# print("Today is a good day to learn Python")
# print('Python is fun')
# print("Python's string are easy to use")
# print('We can even include "quotes" in strings')
# print("Hello" + " world")
# greeting = "hello"
# name = "Alex"
# print()
# print(greeting + ' ' + name)

# print()

# age = 33
# print(age)

# print ()

# print(type(greeting))
# print(type(age))

# age = "2 years"
# print(age)
# print(type(age))

# Section 3:23
# Python is a Strongly Typed Language

# print()
# print("Today is a good day to learn Python")
# print('Python is fun')
# print("Python's string are easy to use")
# print('We can even include "quotes" in strings')
# print("Hello" + " world")
# greeting = "hello"
# name = "Alex"
# print()
# print(greeting + ' ' + name)

# print()

# age = 33
# print(age)

# print ()

# print(type(greeting))
# print(type(age))

# age_in_words = "2 years"
# # print(name + " is " + age + " years old") // errors because of TypeError: can only concatenate str (not "int") to str

# # correct way to print "print(name + " is " + age + " years old")"

# msg = name + " is " + str(age) + " years old"

# print(msg)


# Section 3:30
# slicing

# parrot = "Norwegian Blue"

# print(parrot[0:6]) #Norweg
# print(parrot[3:5])
# print(parrot[0:9])
# print(parrot[:9])

# print(parrot[10:14])
# print(parrot[10:])

# print(parrot[:6] + parrot[6:])

# print(parrot[:])


# Section 3:31
# Slicing with Negative Numbers

# parrot = "Norwegian Blue"

# print(parrot[0:6])

# print(parrot[-4:-2]) # BL
# print(parrot[-4:12]) # BL

# print(parrot[-14:-8])


# Section 3:32
# using Step in a slice

# parrot = "Norwegian Blue"

# print(parrot[0:6:2])

# number = "9,223;372:036 854,775;807"

# seperators = number[1::4]
# print(seperators)

# values = "".join(char if char not in seperators else " " for char in number).split()
# print([int(val) for val in values])

# section 3:33
# slicing backwards

# letters = "abcdefghijklmnopqrstuvwxyz"

# backwards = letters [::-1]
# print(backwards)

# # qpo
# print(letters[-12:-9])
# print(letters[16:13:-1])
# # edcba
# print(letters[4::-1])

# # last 8 characters
# print(letters[:-9:-1])
# print(letters[-4:])
# print(letters[-1:])
# print(letters[:1]) # does not give an error if the string is empty

# empty_str = ""

# print(empty_str[:1]) # no error

# Section 3:35
# String Operators

# string1 = "he's "
# string2 = "probably "
# string3 = "pining "
# string4 = "for the "
# string5 = "fjords"

# print(string1 + string2 + string3 + string4 + string5)

# print("he's " "probably " "pining " "for the " "fjords")

# print("hello " * 5)

# print("Hello " * (5 + 4))
# print("Hello " * 5 + "4")

# today = "friday"
# print("day" in today) # true
# print("fri" in today) # true
# print("thur" in today) # false
# print("parrot" in "fjord") # false

# Section 3:36
# String Replacement Fields

# age = 24
# print("my age is " + str(age) + " years")

# # dot format method
# print("My age is {0} years".format(age))

# print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, and {7}"
#       .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

# print("There are {0} days in Jan, Mar, May, Jul, Aug, Oct, and Dec".format(31))

# print("Jan: {2}, Feb: {0}, Mar: {2}, April: {1}, May: {2}, June: {1}, July: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}"
#       .format(28, 30, 31))


# print("""
# Jan:   {2}
# Feb:   {0}
# Mar:   {2}
# April: {1}
# May:   {2}
# June:  {1}
# July:  {2}
# Sep:   {1}
# Oct:   {2}
# Nov:   {1}
# Dec:   {2}""".format(28, 30, 31))


# section 3:37
# String Formatting

# for i in range(1, 13):
#       print("No. {0:2} squared is {1:3} and cubed {2:4}".format(i, i ** 2, i ** 3))

# print()

# for i in range(1, 13):
#       print("No. {0:2} squared is {1:<3} and cubed {2:<4}".format(i, i ** 2, i ** 3))

# print()

# for i in range(1, 13):
#       print("No. {0:2} squared is {1:<3} and cubed {2:^4}".format(i, i ** 2, i ** 3))

# print()

# print("Pi is approximately {0:12}".format(22/7))
# print("Pi is approximately {0:12f}".format(22/7))
# print("Pi is approximately {0:12.50f}".format(22/7))
# print("Pi is approximately {0:52.50f}".format(22/7))
# print("Pi is approximately {0:62.50f}".format(22/7))
# print("Pi is approximately {0:72.50f}".format(22/7))
# print("Pi is approximately {0:<72.54f}".format(22/7))

# print()

# for i in range(1, 13):
#       print("No. {} squared is {} and cubed {:4}".format(i, i ** 2, i ** 3))

# section 3:38
# f - strings

# name = "Alex"
# greeting = "Hello"
# print(greeting + name)

# # if we want a space, we can add that too
# print(greeting + " " + name)

# age = 24
# print(age)

# print(type(greeting))
# print(type(age))

# age_in_words = "2 years"
# print(name + f" is {age} years old")
# print(type(age))

# print(f"Pi is approximately {22/7:12.50f}")
# pi = 22/7

# print(f"Pi is approximately {pi:12.50f}")

# section 3:39
# Python 2 strings interpolation

# age = 24
# print("My age is %d years" % age)

# major = "years"
# minor = "months"
# print("My age is %d %s, %d %s" % (age, major, 6, minor))
# print("PI is approximately %f" %(22/7))
# print("PI is approximately %60.50f" %(22/7))

# data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
# print(data[1:5])

# print()
# print("Python | Alexander")
# print()

# data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
# print(data[1:5])
# print()

# data2 = "alexander"
# print(data2[0:4])