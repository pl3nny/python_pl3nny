letters = "abcdefghijklmnopqrstuvwxyz"
#          01234567890123456789012345 
backwards = letters[::-1]

print()
print(letters)
print()
print(backwards)
print()


#Challenge
'''
Using the letters string from the video, add some code to create the following  slices.

1. Create a slice that produces the characters qpo.
2. slice the string to produce edcba.
3. Slice the string to produce te last 8 charactes, in reverse order.

'''

print(letters[16:13:-1])  # qpo
print(letters[4::-1]) #edcba
print(letters[25:17:-1])  # last 8 characters in reverse order