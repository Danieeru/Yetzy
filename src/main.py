import random

class ArraySizeError(Exception):
    "Invalid array size"
    pass

class NumberRangeError(Exception):
    "The number is not in the desired range"
    pass

class DuplicateNumberError(Exception):
    "The numbr is already found in the array"
    pass

def validate_array(arr):
    if len(arr) > 5:
        raise ArraySizeError("The length of the array must not be greater than 5")
    for num in arr:
        if not 1 <= num <= 5:
            raise NumberRangeError("The number should be in range from 1 to 5")
    if len(arr) != len(set(arr)):
        raise DuplicateNumberError("The array should not contain duplicate numbers")


def create_object_dice(die_face):
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
    return faces[die_face - 1]
    
# face = create_object_dice(DICE_DATA, number)
    
def print_dice(face):
    print("\n".join(face))

def roll_five_dice() -> list[int]:
    results = []
    for _ in range(5):
        die = random.randint(1, 6)
        results.append(die)
    return results

def reroll_few_dice(result: list[int], reroll_dices: list[int]):
    for die in reroll_dices:
        new_result = random.randint(1, 6)
        result[die - 1] = new_result


def one_turn():
    print("Rolling five dice...")
    result = roll_five_dice()
    print(f"Result: {result}")
    for die in result:
        face = create_object_dice(die)
        print_dice(face)
    for i in range(2):
        print(f"{i + 1}: Rerolling...")
        try:
            reroll_dices = list(map(int, input().split(" ")))
            reroll_few_dice(result, reroll_dices)
            print(f"Updated result: {result}")
            for die in result:
                face = create_object_dice(die)
                print_dice(face)
        except ArraySizeError as e:
            print(f"Size Error: {e}")
        except NumberRangeError as e:
            print(f"Range Error: {e}")
        except DuplicateNumberError as e:
            print(f"Uniqueness Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

def main():
    one_turn()
    # print("Rolling five dice...")
    # results = roll_five_dice()
    # print(f"Results: {results}")
    # for die in results:
    #     face = create_object_dice(die)
    #     print_dice(face)
    # print("\nRerolling a few dice... 1 and 4")
    # # try:
    # reroll_dices = list(map(int, input().split(" ")))
    # # except

    # reroll_few_dice(results, reroll_dices)
    # print(f"Updated results: {results}")
    # for die in results:
    #     die_object = die
    #     die_object.print_dice()




if __name__ == "__main__":
    main()