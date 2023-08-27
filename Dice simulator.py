import random

def roll_dice(num_dice, num_sides):
    rolls = []
    for _ in range(num_dice):
        roll = random.randint(1, num_sides)
        rolls.append(roll)
    return rolls

# Get input from the user
num_dice = int(input("Enter the number of dice to roll: "))
num_sides = int(input("Enter the number of sides on each die: "))

# Roll the dice
dice_rolls = roll_dice(num_dice, num_sides)

# Display the results
print("You rolled:", ', '.join(str(roll) for roll in dice_rolls))
print("Total:", sum(dice_rolls))
