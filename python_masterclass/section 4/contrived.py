numbers = [1,45,31,12,60]

print(numbers)

for num in numbers:
  if num % 8 == 0:
    # reject the list
    print("The numbers are unacceptable")
    break
# else is associated with the for-loop
else:
  print("All those numbers are fine")
  