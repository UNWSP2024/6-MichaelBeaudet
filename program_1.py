# Author: Michael Beaudet
# Title: Week 6 Program 1
# Date: 2/24/25

import random
# setup the dice logic and add them together
def randDice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2

def main():
    total = 0
    rolls = 100
# Run the for loop 100 times 
    for _ in range(rolls):
        total += randDice()

# calculate and display the average 
    average = total / rolls
    print(f"The average of the 100 rolls is: {average:.2f}")

main()
