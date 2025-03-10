import random


class Dice():
    DICE_DATA = """+ - - - - +,+ - - - - +,+ - - - - +,+ - - - - +,+ - - - - +,+ - - - - +
|         |,|  o      |,|  o      |,|  o   o  |,|  o   o  |,|  o   o  |
|    o    |,|         |,|    o    |,|         |,|    o    |,|  o   o  |
|         |,|      o  |,|      o  |,|  o   o  |,|  o   o  |,|  o   o  |
+ - - - - +,+ - - - - +,+ - - - - +,+ - - - - +,+ - - - - +,+ - - - - +
"""
    faces = [[] for _ in range(6)]
    for line in DICE_DATA.splitlines():
        for i, section in enumerate(line.split(',')):
            faces[i].append(section)
    def __init__(self, number):
        self.number = number
    
    def print_dice(self):
        print("\n".join(Dice.faces[self.number - 1]))



def roll_five_dice() -> list[int]:
    results = []
    for _ in range(5):
        die = Dice(random.randint(1, 6))
        results.append(die.number)
    return results

def reroll_few_dice(result: list[int], *ndice: int):
    """В параметрах номер костей, которые нужно перебросить)"""
    for die in ndice:
        new_result = Dice(random.randint(1, 6))
        result[die - 1] = new_result.number

        




def main():
    print("Rolling five dice...")
    results = roll_five_dice()
    print(f"Results: {results}")
    for die in results:
        die_object = Dice(die)
        die_object.print_dice()
    print("\nRerolling a few dice... 1 and 4")
    reroll_dices = list(map(int, input().split(" ")))

    reroll_few_dice(results, reroll_dices)
    print(f"Updated results: {results}")
    for die in results:
        die_object = Dice(die)
        die_object.print_dice()




if __name__ == "__main__":
    main()