import random

def roll_dice():
    return random.randint(1, 6)

number = roll_dice()

while number != 6:
    print(number)
    number = roll_dice()

print(number)
