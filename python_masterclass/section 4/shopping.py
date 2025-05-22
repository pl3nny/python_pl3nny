shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

# for item in shopping_list:
#     if item == "spam":
#         continue

#     print("Buy " + item)


#OUTPUT
# Buy milk
# Buy pasta
# Buy eggs
# Buy bread
# Buy rice

item_to_find = "spam"
found_at = None

# # len() - returns the length of the list
# for index in range(len(shopping_list)):
#   if shopping_list[index] == item_to_find:
#     found_at = index
#     break

if item_to_find in shopping_list:
  found_at = shopping_list.index(item_to_find)

if found_at is not None:
  print("Item found at position {}".format(found_at))
else:
  print("Item {} not in shopping list..".format(item_to_find))