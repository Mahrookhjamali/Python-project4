import random
def roll_dice():
    return random.randint(1,6)
print("Rolling the dice...")
print(f"your rolled a{roll_dice()}")