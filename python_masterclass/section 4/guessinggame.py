# answer = 5

# print("please guess the number between 1 and 10: ")
# guess = int(input())

# # if guess < answer:
# #     print("Please guess higher")
# #     guess = int(input())
# #     if guess == answer:
# #         print("Well done you guessed it")
# #     else:
# #         print("Sorry, you have not guessed correctly")
# # elif guess > answer:
# #     print("Please guess lower")
# #     guess = int(input())
# #     if guess == answer:
# #         print("Well done you guessed it")
# #     else:
# #         print("Sorry, you have not guessed correctly")
# # else:
# #     print("You got it first time")

# if guess != answer:
#     if guess < answer:
#         print("please guess higher")
#     else:   # guess must be greater than answer
#         print("please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("you git it first time")

# looping back to this file in section 4.70

import random

highest = 10
answer = random.randint(1, highest)
print(answer)

guess = None

print("Game start")
print()
print("Guess the Number: ")
guess = int(input())

if guess == answer:
  print("You GUESSED IT!")

while guess != answer:

  if guess == answer:
    print("You GUESSED IT!")
    break
  elif guess == 0:
    print("you've quit the game..")
    break
  else:
    answer = random.randint(1,highest)
    print(answer)
  
  guess = int(input("guess again: "))

print("program terminated...")