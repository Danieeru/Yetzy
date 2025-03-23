import random
# import pandas as pd
# import numpy as np
import sys

class ArraySizeError(Exception):
    "Invalid array size"
    pass

class NumberRangeError(Exception):
    "The number is not in the desired range"
    pass

class DuplicateNumberError(Exception):
    "The number is already found in the array"
    pass

def validate_array(arr):
    if len(arr) > 5:
        raise ArraySizeError("The length of the array must not be greater than 5")
    arr = list(arr.replace(" ", ""))
    for num in arr:
        if not num.isdigit():
            raise InvalidArgumentError("The numbers must be")
    arr = list(map(int, arr))
    for num in arr:
        if not 1 <= num <= 6:
            raise NumberRangeError("The numbers should be in range from 1 to 6")
    return arr

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

  
def print_five_dice(result):
    faces = [create_object_dice(die) for die in result]
    for i in range(len(faces)):
        for j in range(len(faces[0])):
            print(faces[j][i], end=' ')
        print()


def roll_five_dice() -> list[int]:
    results = []
    for _ in range(5):
        die = random.randint(1, 6)
        results.append(die)
    return results

def reroll_few_dice(result: list[int], reroll_dices: list[int]):
    new_result = []
    for num in result:
        if num in reroll_dices:
            new_result.append(reroll_dices.pop(reroll_dices.index(num)))
        elif num not in reroll_dices:
            new_result.append(random.randint(1, 6))
    for i in range(len(new_result)):
        result[i] = new_result[i]


def one_turn():
    print("Rolling five dice...")
    result = roll_five_dice()
    # print(f"Result: {result}")
    check_all_combinations(result)
    print_five_dice(result)
    for i in range(2):
        print(f"{i + 1}: Rerolling...")
        try:
            reroll = input()
            reroll = validate_array(reroll)
            reroll_few_dice(result, reroll)
            print(f"Updated result: {result}")
            check_all_combinations(result)
            print_five_dice(result) 
        except ArraySizeError as e:
            print(f"Size Error: {e}")
        except NumberRangeError as e:
            print(f"Range Error: {e}")
        except DuplicateNumberError as e:
            print(f"Uniqueness Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")


def add_players():
    players = []
    count_players = int(input("Количество игроков: "))
    if count_players < 1 or count_players > 4:
        print("Количество игроков должно быть между 1 и 4.")
        return
    for i in range(count_players):
        player_name = input(f"Имя игрока {i + 1}: ")
        players.append(player_name)
    return players


def create_start_table(combinations_ru, players):
    count_players = len(players)
    for comb, player in combinations_ru.items():
        for i in range(count_players):
            if comb == "64/35":
                player.append(players[i])
            else:
                player.append("")


def draw_table(combinations_ru, players):
    count_players = len(players)
    max_name = max(len(name) for name in players)
    sys.stdout.write("\033[F" * (count_players - 25))
    for comb, player in combinations_ru.items():
        print("+" + "-" * 17 + ("+" + "-" * (max_name + 4)) * count_players + "+")
        print(f"| {comb:^15} |", end="")
        for i in range(count_players):
            print(f" {player[i]:^{max_name + 2}} |",end="")
        print()


def two_pairs_check(result):
    counts = {}
    s = 0
    for num in result:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
    temp = -1
    for num, count in counts.items():
        if count >= 2 and temp == -1:
            temp = num
        elif count >= 2 and temp != 1:
            s = temp * 2 + num * 2
    return s
            

def full_house_check(result):
    counts = {}
    for num in result:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
    s = 0
    if len(counts) == 2:
        for num, count in counts.items():
            if count == 2 or count == 3:
                s += num * count
    return s
        
    
def small_straight_check(result):
    counts = {}
    temp = result.copy()
    temp.sort()
    n = len(temp)
    res = 0
    for i in range(n - 3):
        sub = temp[i:i+4]
        valid = True
        for j in range(3):
            if sub[j + 1] != sub[j] + 1:
                valid = False
                break
        if valid:
            s = sum(sub)
            if s > res:
                res = s
    return res


def large_straight_check(result):
    counts = {}
    temp = result.copy()
    temp.sort()
    n = len(temp)
    res = 0
    for i in range(n - 4):
        sub = temp[i:i+5]
        valid = True
        for j in range(4):
            if sub[j + 1] != sub[j] + 1:
                valid = False
                break
        if valid:
            s = sum(sub)
            if s > res:
                res = s
    return res

def chance_check(dices):
    return sum(dices)

def number_check(dices, number):
    number_in_dices = dices.count(number)
    return number_in_dices * number

def number_of_a_kind_check(dices, number):
    counts = {}
    for num in dices:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
    res = 0
    for num, count in counts.items():
        if count >= number:
            s = number * num
            if s > res: res = s
    return res


def check_all_combinations(result):
    res = {
        "1": number_check(result, 1),
        "2": number_check(result, 2),
        "3": number_check(result, 3),
        "4": number_check(result, 4),
        "5": number_check(result, 5),
        "6": number_check(result, 6),
        "Пара": number_of_a_kind_check(result, 2),
        "Две пары": two_pairs_check(result),
        "Сет": number_of_a_kind_check(result, 3),
        "Каре": number_of_a_kind_check(result, 4),
        "Фулл Хаус": full_house_check(result),
        "Малый стрит": small_straight_check(result),
        "Большой стрит": large_straight_check(result),
        "Ецци": number_of_a_kind_check(result, 5),
        "Шанс": chance_check(result)
    }
    res = dict(reversed(sorted(res.items(), key=lambda item: item[1])))
    for comb, r in res.items():
        if r == 0:
            continue
        else:
            print(comb, r)
def main():
    combinations_ru = {
        "64/35": [],
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": [],
        "6": [],
        "Пара": [],
        "2 пары": [],
        "Сет": [],
        "Каре": [],
        "Фулл хаус": [],
        "Малый стрит": [],
        "Большой стрит": [],
        "Ецци": [],
        "Шанс": [],
        "Сумма": []
        }
    print("Welcome to Yezzi!")
    players = add_players()
    count_players = len(players)
    create_start_table(combinations_ru, players)
    print("Starting grid:")
    draw_table(combinations_ru, players)
    turn = 1
    while True:
        print(f"Turn {turn}")
        for i in range(len(players)):
            print(f"{players[i]}:")
            one_turn()
            # функция записи
            # функция печати измененной таблицы

        turn += 1





if __name__ == "__main__":
    main()