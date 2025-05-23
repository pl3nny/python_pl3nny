available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
  chosen_exit = input("Please choose the direction: ")

  if chosen_exit.casefold() == "quit":
    print("game over")
    break
  elif chosen_exit in available_exits:
    print("Aren't you glad you got out of there")


print()
print("Program terminated")