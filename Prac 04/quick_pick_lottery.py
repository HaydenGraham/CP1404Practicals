import random

rows = int(input("How many quick picks? "))
# rows = 5
for i in range(0, rows):
    row = [random.randint(1, 45)]
    while len(row) < 6:
        number = random.randint(1, 45)
        if not (number in row):
            row += [number]
    row.sort()

    print("{0:>2} {1:>2} {2:>2} {3:>2} {4:>2} {5:>2}".format(*row))
