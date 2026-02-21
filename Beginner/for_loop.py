import random

count_6 = 0
for i in range(20):
    roll = random.randint(1,6)
    if roll == 6:
        count_6 += 1

print("Total 6s:", count_6)
