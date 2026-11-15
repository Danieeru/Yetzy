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
from collections import Counter

class Dice:
    def __init__(self):
        self.faces = [
        ["+ - - - - +", "|         |", "|    o    |", "|         |", "+ - - - - +"],
        ["+ - - - - +", "|  o      |", "|         |", "|      o  |", "+ - - - - +"],
        ["+ - - - - +", "|  o      |", "|    o    |", "|      o  |", "+ - - - - +"],
        ["+ - - - - +", "|  o   o  |", "|         |", "|  o   o  |", "+ - - - - +"],
        ["+ - - - - +", "|  o   o  |", "|    o    |", "|  o   o  |", "+ - - - - +"],
        ["+ - - - - +", "|  o   o  |", "|  o   o  |", "|  o   o  |", "+ - - - - +"],
    ]
        self.escape = 'q'
        self.dices = []
        self.reroll_dices = []
        self.count_roll = 3
        self.count_dices = 5
    
    def print_five_dices(self) -> None:
        """Print ASCII representation of five dice in a row."""
        faces = [self.create_object_dice(dice) for dice in self.dices]
        for i in range(len(faces)):
            for j in range(len(faces[0])):
                print(faces[j][i], end=' ')
            print()
    
    def create_object_dice(self, dice_face: int) -> list[str]:
        """Create ASCII representation of a dice face (1-6)."""
        return self.faces[dice_face - 1]
                
    def roll_five_dices(self) -> None:
        """Generate five random dices rolls (1-6)."""
        self.dices = [random.randint(1, 6) for _ in range(self.count_dices)]
        
    def reroll_few_dice(self) -> None:
        """Reroll specified dice while keeping others unchanged."""
        if self.reroll_dices == self.escape:
            return
        new_dices = []
        for num in self.dices:
            if num in self.reroll_dices:
                new_dices.append(self.reroll_dices.pop(self.reroll_dices.index(num)))
            elif num not in self.reroll_dices:
                new_dices.append(random.randint(1, 6))
        for i, dice in enumerate(new_dices):
            self.dices[i] = dice
            
    def get_valid_dices(self):
        count_res = Counter(self.dices)
        while True:
            user_input = input("Keep: ")
            if user_input == self.escape:
                return self.escape
            if not user_input:
                return []
            if not user_input.isdigit():
                print("Error! Must be integers only")
                continue
            elements = list(map(int, list(user_input.replace(" ", ""))))
            if len(elements) > 5:
                print("Error! Cannot keep more tham five dice")
                continue
            if not all(1 <= elem <= 6 for elem in elements):
                print("Error! Number must be between 1 and 6.")
                continue
            requested_count = Counter(elements)
            for num, count in requested_count.items():
                if count_res[num] < count:
                    print("Error! No such dice!")
                    break
            else:
                self.reroll_dices = elements
                return