print("Today is a good day to learn Python")
print('Python is fun')
print("Python's string are easy to use")
print('We can even include "quotes" in strings')
print("Hello" + " world")

greeting = "Hello"
name = input("please enter your name: ")
print(greeting + name)
# if we want a space, we can add that too
print(greeting + ' ' + name)

age = 24
print(age)

print(type(greeting))
print(type(age))

age = "2 years"

print(age)
print(type(age))

age_in_words = "2 years"
print(name + " is " + age + " years old")
print(type(age))

print()
print(name + f" is {age} years old")
print()
print(f"Pi is approximately {22/7:12.50f}")
print()
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")