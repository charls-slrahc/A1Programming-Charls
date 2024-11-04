# loop that counts up from 0 to 50 in increments of 1

print("Counting up from 0 to 50:")
for i in range(0, 51, 1):
    print(i, end=' ')
print ("\n")

# loop that counts down from 50 to 0 in decrements of 1

print("Counting down from 50 to 0:")
for i in range(50, -1, -1):
    print(i, end=' ')
print("\n")

# loop the counts up from 30 to 50 in increments 0f 1 

print("counting up from 30 to 50")
for i in range(30, 51, 1):
    print(i, end=' ')
print("\n")

#loop that counts down from 50 to 10 with decrements of 2

loop4 = 50
while loop4 >= 10:
    loop4 -= 2
    print(loop4)
    if loop4 == 10: break