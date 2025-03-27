import random
import sys


def get_valid_number() -> int:
    while True:
        user_input = input("Количество игроков: ").strip()
        if not user_input:
            print("Ошибка! Введите не пустое значение")
            continue
        try:
            number = int(user_input)
            if 1 <= number <= 6:
                return number
            print("Ошибка! Количество игроков может быть от 1 до 6")
        except ValueError:
            print("Ошибка '{user_input}' не является целым числом")


def get_valid_array(dice: list[int]) -> list[int]:
    count_res = {}
    for num in dice:
        if num in count_res:
            count_res[num] += 1
        else:
            count_res[num] = 1
    while True:
        user_input = input("Оставить: ")
        if user_input == "з":
            return "з"
        if not user_input:
            return []
        elements = list(user_input.replace(" ", ""))
        if len(elements) > 5:
            print("Ошибка! Нельзя оставить больше пяти костей")
            continue
        val_nums = []
        val_nums_count = {}
        for elem in elements:
            try:
                number = int(elem)
                if 1 <= number <= 6:
                    val_nums.append(number)
                else:
                    print("Ошибка! Число не входит в диапазон 1 - 6")
                    break
            except ValueError:
                print("Ошибка! Должны быть только целые числа")
                break
        else:
            for num in val_nums:
                if num in val_nums_count:
                    val_nums_count[num] += 1
                else:
                    val_nums_count[num] = 1
            for num, count in val_nums_count.items():
                if num not in count_res or count > count_res[num]:
                    print("Ошибка! Таких костей нет!")
                    break
            else:
                return val_nums


def create_object_dice(die_face: int) -> list[str]:
    faces = [
        ["+ - - - - +", "|         |", "|    o    |", "|         |", "+ - - - - +"],
        ["+ - - - - +", "|  o      |", "|         |", "|      o  |", "+ - - - - +"],
        ["+ - - - - +", "|  o      |", "|    o    |", "|      o  |", "+ - - - - +"],
        ["+ - - - - +", "|  o   o  |", "|         |", "|  o   o  |", "+ - - - - +"],
        ["+ - - - - +", "|  o   o  |", "|    o    |", "|  o   o  |", "+ - - - - +"],
        ["+ - - - - +", "|  o   o  |", "|  o   o  |", "|  o   o  |", "+ - - - - +"],
    ]
    return faces[die_face - 1]


def print_five_dice(dice: list[int]):
    faces = [create_object_dice(die) for die in dice]
    for i in range(len(faces)):
        for j in range(len(faces[0])):
            print(faces[j][i], end=' ')
        print()


def roll_five_dice() -> list[int]:
    dice = []
    for _ in range(5):
        die = random.randint(1, 6)
        dice.append(die)
    return dice

def reroll_few_dice(dice: list[int], reroll_dices: list[int]):
    if reroll_dices == "з":
        return
    new_dice = []
    for num in dice:
        if num in reroll_dices:
            new_dice.append(reroll_dices.pop(reroll_dices.index(num)))
        elif num not in reroll_dices:
            new_dice.append(random.randint(1, 6))
    for i, die in enumerate(new_dice):
        dice[i] = die


def one_turn() -> dict[str]:
    print("Rolling five dice...")
    dice = roll_five_dice()
    print_five_dice(dice)
    res = check_all_combinations(dice)
    for i in range(2):
        print(f"{i + 1}: Rerolling...")
        reroll = get_valid_array(dice)
        reroll_few_dice(dice, reroll)
        print(f"Updated dice: {dice}")
        print_five_dice(dice)
        res = check_all_combinations(dice)
    return res


def add_players(count_players):
    players = []
    for i in range(count_players):
        while True:
            player_name = input(f"Имя игрока {i + 1}: ")
            if not player_name:
                print("Ошибка! Имя не может быть пустым")
            else:
                players.append(player_name)
                break
    return players


def create_start_table(combinations_ru, players):
    count_players = len(players)
    for comb, player in combinations_ru.items():
        for i in range(count_players):
            if comb == "64/35":
                player.append(players[i])
            elif comb == "Сумма":
                player.append(0)
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


def two_pairs_check(dice):
    counts = {}
    s = 0
    for num in dice:
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


def full_house_check(dice):
    counts = {}
    for num in dice:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
    s = 0
    if len(counts) == 2:
        for num, count in counts.items():
            if count in (2, 3):
                s += num * count
    return s


def small_straight_check(dice: list[int]):
    res = 0
    dices_unique = list(set(sorted(dice)))
    if len(dices_unique) >= 4:
        for i in range(len(dices_unique) - 3):
            flag = True
            s = 0
            for j in range(3):
                if dices_unique[i + j + 1] != dices_unique[i + j] + 1:
                    flag = False
                    break
            if flag:
                for j in range(4):
                    s += dices_unique[i + j]
                res = max(res, s)
    return res


def large_straight_check(dice):
    temp = dice.copy()
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
            res = max(res, s)
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
            res = max(res, s)
    return res


def check_all_combinations(dice):
    res = {
        "Один": number_check(dice, 1),
        "Два": number_check(dice, 2),
        "Три": number_check(dice, 3),
        "Четыре": number_check(dice, 4),
        "Пять": number_check(dice, 5),
        "Шесть": number_check(dice, 6),
        "Пара": number_of_a_kind_check(dice, 2),
        "Две Пары": two_pairs_check(dice),
        "Сет": number_of_a_kind_check(dice, 3),
        "Каре": number_of_a_kind_check(dice, 4),
        "Фулл Хаус": full_house_check(dice),
        "Малый Стрит": small_straight_check(dice),
        "Большой Стрит": large_straight_check(dice),
        "Ецци": number_of_a_kind_check(dice, 5),
        "Шанс": chance_check(dice)
    }
    res = dict(reversed(sorted(res.items(), key=lambda item: item[1])))
    for comb, r in res.items():
        if r != 0:
            print(f"| {comb}: {r} ", end="")
        else:
            continue
    print("|", end="\n")
    return res


def write_res_in_table(combinations_ru, res, player, block_nums: list[int], block_num_bool: list[bool]):
    while True:
        com_input = input("Запись: ").lower().strip().replace(" ", "")
        if com_input in ("1", "один"):
            if combinations_ru["Один"][player] == "":
                combinations_ru["Один"][player] = res["Один"]
                combinations_ru["Сумма"][player] += res["Один"]
                block_nums[player] += res["Один"]
            else:
                print("Ошибка! Результат уже записан.")
                continue
        elif com_input in ("2", "два"):
            if combinations_ru["Два"][player] == "":
                combinations_ru["Два"][player] = res["Два"]
                combinations_ru["Сумма"][player] += res["Два"]
                block_nums[player] += res["Два"]
            else:
                print("Ошибка! Результат уже записан.")
                continue
        elif com_input in ("3", "три"):
            if combinations_ru["Три"][player] == "":
                combinations_ru["Три"][player] = res["Три"]
                combinations_ru["Сумма"][player] += res["Три"]
                block_nums[player] += res["Три"]
            else:
                print("Ошибка! Результат уже записан.")
                continue
        elif com_input in ("4", "четыре"):
            if combinations_ru["Четыре"][player] == "":
                combinations_ru["Четыре"][player] = res["Четыре"]
                combinations_ru["Сумма"][player] += res["Четыре"]
                block_nums[player] += res["Четыре"]
            else:
                print("Ошибка! Результат уже записан.")
                continue
        elif com_input in ("5", "пять"):
            if combinations_ru["Пять"][player] == "":
                combinations_ru["Пять"][player] = res["Пять"]
                combinations_ru["Сумма"][player] += res["Пять"]
                block_nums[player] += res["Пять"]
            else:
                print("Ошибка! Результат уже записан.")
                continue
        elif com_input in ("6", "шесть"):
            if combinations_ru["Шесть"][player] == "":
                combinations_ru["Шесть"][player] = res["Шесть"]
                combinations_ru["Сумма"][player] += res["Шесть"]
                block_nums[player] += res["Шесть"]
            else:
                print("Ошибка! Результат уже записан.")
                continue
        elif com_input in ("пара", "п"):
            if combinations_ru["Пара"][player] == "":
                combinations_ru["Пара"][player] = res["Пара"]
                combinations_ru["Сумма"][player] += res["Пара"]
            else:
                print("Ошибка! Результат уже записан.")
                continue
        elif com_input in ("двепары", "пп"):
            if combinations_ru["Две Пары"][player] == "":
                combinations_ru["Две Пары"][player] = res["Две Пары"]
                combinations_ru["Сумма"][player] += res["Две Пары"]
            else:
                print("Ошибка! Результат уже записан.")
                continue
        elif com_input in ("сет", "с"):
            if combinations_ru["Сет"][player] == "":
                combinations_ru["Сет"][player] = res["Сет"]
                combinations_ru["Сумма"][player] += res["Сет"]
            else:
                print("Ошибка! Результат уже записан.")
                continue
        elif com_input in ("каре", "к"):
            if combinations_ru["Каре"][player] == "":
                combinations_ru["Каре"][player] = res["Каре"]
                combinations_ru["Сумма"][player] += res["Каре"]
            else:
                print("Ошибка! Результат уже записан.")
                continue
        elif com_input in ("фуллхаус", "ф", "фх"):
            if combinations_ru["Фулл Хаус"][player] == "":
                combinations_ru["Фулл Хаус"][player] = res["Фулл Хаус"]
                combinations_ru["Сумма"][player] += res["Фулл Хаус"]
            else:
                print("Ошибка! Результат уже записан.")
                continue 
        elif com_input in ("малыйстрит", "м", "мс"):
            if combinations_ru["Малый Стрит"][player] == "":
                combinations_ru["Малый Стрит"][player] = res["Малый Стрит"]
                combinations_ru["Сумма"][player] += res["Малый Стрит"]
            else:
                print("Ошибка! Результат уже записан.")
                continue 
        elif com_input in ("большойстрит", "б", "бс"):
            if combinations_ru["Большой Стрит"][player] == "":
                combinations_ru["Большой Стрит"][player] = res["Большой Стрит"]
                combinations_ru["Сумма"][player] += res["Большой Стрит"]
            else:
                print("Ошибка! Результат уже записан.")
                continue
        elif com_input in ("ецци", "е"):
            if combinations_ru["Ецци"][player] == "":
                combinations_ru["Ецци"][player] = res["Ецци"]
                combinations_ru["Сумма"][player] += res["Ецци"]
            else:
                print("Ошибка! Результат уже записан.")
                continue
        elif com_input in ("шанс", "ш"):
            if combinations_ru["Шанс"][player] == "":
                combinations_ru["Шанс"][player] = res["Шанс"]
                combinations_ru["Сумма"][player] += res["Шанс"]
            else:
                print("Ошибка! Результат уже записан.")
                continue
        else:
            print("Ошибка! Нет такой команды!")
            continue
        break
    if block_nums[player] >= 64 and block_num_bool[player] is False:
        block_num_bool[player] = True
        combinations_ru["Сумма"][player] += 35
        print("БЛОК СОБРАН! +35")


def calc_cell(combinations_ru):
    s = 0
    for comb, scores in combinations_ru.items():
        if comb in ("64/35", "Сумма"):
            continue
        s += len(scores)
    return s


def main():
    combinations_ru = {
        "64/35": [],
        "Один": [],
        "Два": [],
        "Три": [],
        "Четыре": [],
        "Пять": [],
        "Шесть": [],
        "Пара": [],
        "Две Пары": [],
        "Сет": [],
        "Каре": [],
        "Фулл Хаус": [],
        "Малый Стрит": [],
        "Большой Стрит": [],
        "Ецци": [],
        "Шанс": [],
        "Сумма": []
    }
    print("Welcome to Yezzi!")
    count_players = get_valid_number()
    players = add_players(count_players)
    block_nums = [0 for i in players]
    block_num_bool = [False for i in players]
    create_start_table(combinations_ru, players)
    print("Starting grid:")
    draw_table(combinations_ru, players)
    cells = calc_cell(combinations_ru)
    turn = 1
    while cells >= turn * count_players:
        print(f"Turn {turn}")
        for i, player in enumerate(players):
            print(f"{player}:")
            res = one_turn()
            write_res_in_table(combinations_ru, res, i, block_nums, block_num_bool)
            draw_table(combinations_ru, players)
        turn += 1


if __name__ == "__main__":
    main()
