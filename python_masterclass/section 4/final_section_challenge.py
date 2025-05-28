print("Author: Alexander | Python")
print()

user_input = "-"

while user_input != "0":

  print("Please choose your option from the list below:")
  print("1: Learn Python")
  print("2: Learn Java")
  print("3: Go Swimming")
  print("4: Have dinner")
  print("5: Go to bed")
  print("0: Exit")

  user_input = input("enter option: ")

  # if user_input == 1:
  #   print("Learning Python right now.")
  # elif user_input == 2:
  #   print("learn java later")
  # elif user_input == 3:
  #   print("swimming sounds fun")
  # elif user_input == 4:
  #   print("time to ead dinner")
  # elif user_input == 5:
  #   print("go to bed")
  # else:
  #   print("not a valid option, try again...")

  if user_input == "0":
    break
  elif user_input in "12345":
    print("You chose option {}".format(user_input))
  else:
    print("option not available...try again")