"""
Dice handling module.

Contains functions for creating, displaying and updating dice.
Includes:
- Creating ASCII representation of dice faces
- Displaying five dice in a row
- Rolling five dice
- Rerolling selected dice
"""
import random

def create_object_dice(die_face: int) -> list[str]:
    """Create ASCII representation of a die face (1-6)."""
    faces = [
        ["+ - - - - +", "|         |", "|    o    |", "|         |", "+ - - - - +"],
        ["+ - - - - +", "|  o      |", "|         |", "|      o  |", "+ - - - - +"],
        ["+ - - - - +", "|  o      |", "|    o    |", "|      o  |", "+ - - - - +"],
        ["+ - - - - +", "|  o   o  |", "|         |", "|  o   o  |", "+ - - - - +"],
        ["+ - - - - +", "|  o   o  |", "|    o    |", "|  o   o  |", "+ - - - - +"],
        ["+ - - - - +", "|  o   o  |", "|  o   o  |", "|  o   o  |", "+ - - - - +"],
    ]
    return faces[die_face - 1]


def print_five_dice(dice: list[int]) -> None:
    """Print ASCII representation of five dice in a row."""
    faces = [create_object_dice(die) for die in dice]
    for i in range(len(faces)):
        for j in range(len(faces[0])):
            print(faces[j][i], end=' ')
        print()


def roll_five_dice() -> list[int]:
    """Generate five random dice rolls (1-6)."""
    dice = []
    for _ in range(5):
        die = random.randint(1, 6)
        dice.append(die)
    return dice


def reroll_few_dice(dice: list[int], reroll_dices: list[int]) -> None:
    """Reroll specified dice while keeping others unchanged."""
    if reroll_dices == "q":
        return
    new_dice = []
    for num in dice:
        if num in reroll_dices:
            new_dice.append(reroll_dices.pop(reroll_dices.index(num)))
        elif num not in reroll_dices:
            new_dice.append(random.randint(1, 6))
    for i, die in enumerate(new_dice):
        dice[i] = die
