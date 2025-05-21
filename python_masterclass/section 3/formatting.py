for i in range (1, 13):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

# the :2 and :4 add spaces next to the values
# right align the values

'''
No.  1 squared is    1 and cubed is    1
No.  2 squared is    4 and cubed is    8
No.  3 squared is    9 and cubed is   27
No.  4 squared is   16 and cubed is   64
No.  5 squared is   25 and cubed is  125
No.  6 squared is   36 and cubed is  216
No.  7 squared is   49 and cubed is  343
No.  8 squared is   64 and cubed is  512
No.  9 squared is   81 and cubed is  729
No. 10 squared is  100 and cubed is 1000
No. 11 squared is  121 and cubed is 1331
No. 12 squared is  144 and cubed is 1728
'''

print()

#left align the values
for i in range (1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

'''
No.  1 squared is 1   and cubed is 1   
No.  2 squared is 4   and cubed is 8   
No.  3 squared is 9   and cubed is 27  
No.  4 squared is 16  and cubed is 64  
No.  5 squared is 25  and cubed is 125 
No.  6 squared is 36  and cubed is 216 
No.  7 squared is 49  and cubed is 343 
No.  8 squared is 64  and cubed is 512 
No.  9 squared is 81  and cubed is 729 
No. 10 squared is 100 and cubed is 1000
No. 11 squared is 121 and cubed is 1331
No. 12 squared is 144 and cubed is 1728
'''
print()

#center align the values
for i in range (1, 13):
    print("No. {0:2} squared is {1:^3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))
'''
No.  1 squared is  1  and cubed is  1  
No.  2 squared is  4  and cubed is  8  
No.  3 squared is  9  and cubed is  27 
No.  4 squared is 16  and cubed is  64 
No.  5 squared is 25  and cubed is 125 
No.  6 squared is 36  and cubed is 216 
No.  7 squared is 49  and cubed is 343 
No.  8 squared is 64  and cubed is 512 
No.  9 squared is 81  and cubed is 729 
No. 10 squared is 100 and cubed is 1000
No. 11 squared is 121 and cubed is 1331
No. 12 squared is 144 and cubed is 1728
'''
print()

print("Pi is approximately {0:12}".format(22/7))
print("Pi is approximately {0:12f}".format(22/7))
print("Pi is approximately {0:12.50f}".format(22/7))
print("Pi is approximately {0:52.50f}".format(22/7))
print("Pi is approximately {0:62.50f}".format(22/7))
print("Pi is approximately {0:72.50f}".format(22/7))
print("Pi is approximately {0:<72.54f}".format(22/7))


'''
Pi is approximately 3.142857142857143
Pi is approximately     3.142857
Pi is approximately 3.14285714285714279370154144999105483293533325195312
Pi is approximately 3.14285714285714279370154144999105483293533325195312
Pi is approximately           3.14285714285714279370154144999105483293533325195312
Pi is approximately                     3.14285714285714279370154144999105483293533325195312
Pi is approximately 3.142857142857142793701541449991054832935333251953125000  
'''
print()

for i in range (1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))

'''
No. 1 squared is 1 and cubed is    1
No. 2 squared is 4 and cubed is    8
No. 3 squared is 9 and cubed is   27
No. 4 squared is 16 and cubed is   64
No. 5 squared is 25 and cubed is  125
No. 6 squared is 36 and cubed is  216
No. 7 squared is 49 and cubed is  343
No. 8 squared is 64 and cubed is  512
No. 9 squared is 81 and cubed is  729
No. 10 squared is 100 and cubed is 1000
No. 11 squared is 121 and cubed is 1331
No. 12 squared is 144 and cubed is 1728
'''