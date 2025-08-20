import itertools
import json

# Можно использовать Counter из collections для подсчета уникальных символов в массиве
class CompactArrayEncoder(json.JSONEncoder):
    def iterencode(self, o, _one_shot=False):
        if isinstance(o, list) and all(isinstance(i, (int, float)) for i in o):
            return f"[{','.join(map(str, o))}]"
        elif isinstance(o, list):
            return "[\n" + ",\n".join(
                self.iterencode(item).replace("\n", "\n  ")
                for item in o
            ) + "\n]"
        elif isinstance(o, dict):
            return "{\n" + ",\n".join([
                f'"{k}": {self.iterencode(v).replace("\n", "\n  ")}'
                for k, v in o.items()
            ]) + "\n}"
        return super().iterencode(o, _one_shot)


def generate_dice():
    dice = list(itertools.product("123456", repeat=5))
    for i in range(len(dice)):
        dice[i] = [int(x) for x in dice[i]]
    return dice

def write_to_dict(dict_num, s, arr):
    if s not in dict_num:
        dict_num[s] = []
    dict_num[s].append(arr)


def one_generate(dice):
    num_dict = {}
    num = 1
    for arr in dice:
        count = arr.count(num)
        for temp_count in range(6):
            if count == temp_count == 0:
                write_to_dict(num_dict, 0, arr)
            if count >= temp_count != 0:
                write_to_dict(num_dict, num * temp_count, arr)
    return dict(sorted(num_dict.items()))


def two_generate(dice):
    num_dict = {}
    num = 2
    for arr in dice:
        count = arr.count(num)
        for temp_count in range(6):
            if count == temp_count == 0:
                write_to_dict(num_dict, 0, arr)
            if count >= temp_count != 0:
                write_to_dict(num_dict, num * temp_count, arr)
    return dict(sorted(num_dict.items()))


def three_generate(dice):
    num_dict = {}
    num = 3
    for arr in dice:
        count = arr.count(num)
        for temp_count in range(6):
            if count == temp_count == 0:
                write_to_dict(num_dict, 0, arr)
            if count >= temp_count != 0:
                write_to_dict(num_dict, num * temp_count, arr)
    return dict(sorted(num_dict.items()))


def four_generate(dice):
    num_dict = {}
    num = 4
    for arr in dice:
        count = arr.count(num)
        for temp_count in range(6):
            if count == temp_count == 0:
                write_to_dict(num_dict, 0, arr)
            if count >= temp_count != 0:
                write_to_dict(num_dict, num * temp_count, arr)
    return dict(sorted(num_dict.items()))


def five_generate(dice):
    num_dict = {}
    num = 5
    for arr in dice:
        count = arr.count(num)
        for temp_count in range(6):
            if count == temp_count == 0:
                write_to_dict(num_dict, 0, arr)
            if count >= temp_count != 0:
                write_to_dict(num_dict, num * temp_count, arr)
    return dict(sorted(num_dict.items()))


def six_generate(dice):
    num_dict = {}
    num = 6
    for arr in dice:
        count = arr.count(num)
        for temp_count in range(6):
            if count == temp_count == 0:
                write_to_dict(num_dict, 0, arr)
            if count >= temp_count != 0:
                write_to_dict(num_dict, num * temp_count, arr)
    return dict(sorted(num_dict.items()))


def one_pair_generate(dice):
    num_dict = {}
    for arr in dice:
        counts = {}
        found = False
        for num in arr:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        for num, count in counts.items():
            if count >= 2:
                found = True
                s = num * 2
                write_to_dict(num_dict, s, arr)
        if not found:
            write_to_dict(num_dict, 0, arr)

    return dict(sorted(num_dict.items()))
def two_pair_generate(dice):
    num_dict = {}
    for arr in dice:
        found = False
        counts = {}
        for num in arr:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        temp = -1
        for num, count in counts.items():
            if count >= 2 and temp == -1:
                temp = num
            elif count >= 2 and temp!= -1:
                found = True
                s = temp * 2 + num * 2
                write_to_dict(num_dict, s, arr)
                temp = -1
        if not found:
            write_to_dict(num_dict, 0, arr)
    return dict(sorted(num_dict.items()))
def three_of_a_kind_generate(dice):
    num_dict = {}
    for arr in dice:
        counts = {}
        found = False
        for num in arr:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        for num, count in counts.items():
            if count >= 3:
                found = True
                s = num * 3
                write_to_dict(num_dict, s, arr)
        if not found:
            write_to_dict(num_dict, 0, arr)
    return dict(sorted(num_dict.items()))
def four_of_a_kind_generate(dice):
    num_dict = {}
    for arr in dice:
        found = False
        counts = {}
        for num in arr:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        for num, count in counts.items():
            if count >= 4:
                found = True
                s = num * 4
                write_to_dict(num_dict, s, arr)
        if not found:
            write_to_dict(num_dict, 0, arr)
    return dict(sorted(num_dict.items()))
def full_house_generate(dice):
    # нету нормальной обрабоки случая 4 + 1
    # не работает для n-го количества костей
    num_dict = {}
    for arr in dice:
        found = False
        counts = {}
        for num in arr:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        if len(counts) == 2: # сюда заходят комбинации 4 + 1, нужен апргейд
            s = 0
            for num, count in counts.items():
                if count == 2 or count == 3:
                    found = True
                    s += num * count
            if s != 0:
                write_to_dict(num_dict, s, arr)
        if not found:
            write_to_dict(num_dict, 0, arr)
    return dict(sorted(num_dict.items()))

def small_straight_generate(dice):
    num_dict = {}
    for arr in dice:
        temp_arr = arr.copy()
        temp_arr.sort()
        found = False
        n = len(temp_arr)
        for i in range(n - 3):
            subarray = temp_arr[i:i+4]
            valid = True
            for j in range(3):
                if subarray[j + 1] != subarray[j] + 1:
                    valid = False
                    break
            if valid:
                s = sum(subarray)
                found = True
                write_to_dict(num_dict, s, arr)
        if not found:
            write_to_dict(num_dict, 0, arr)
    return dict(sorted(num_dict.items()))


def large_straight_generate(dice):
    num_dict = {}
    for arr in dice:
        temp_arr = arr.copy()
        temp_arr.sort()
        found = False
        n = len(temp_arr)
        for i in range(n - 4):
            subarray = temp_arr[i:i+5]
            valid = True
            for j in range(4):
                if subarray[j + 1] != subarray[j] + 1:
                    valid = False
                    break
            if valid:
                s = sum(subarray)
                found = True
                write_to_dict(num_dict, s, arr)
        if not found:
            write_to_dict(num_dict, 0, arr)
    return dict(sorted(num_dict.items()))


def yezzi_generate(dice):
    num_dict = {}
    for arr in dice:
        found = False
        counts = {}
        for num in arr:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        for num, count in counts.items():
            if count == 5:
                s = num * 5
                found = True
                write_to_dict(num_dict, s, arr)
        if not found:
            write_to_dict(num_dict, 0, arr)
    return dict(sorted(num_dict.items()))


def chance_generate(dice):
    num_dict = {}
    for arr in dice:
        s = sum(arr)
        write_to_dict(num_dict, s, arr)
    return dict(sorted(num_dict.items()))


def game_data_json(dice):
    try:
        game_data = {
        "one": one_generate(dice),
        "two": two_generate(dice),
        "three": three_generate(dice),
        "four": four_generate(dice),
        "five": five_generate(dice),
        "six": six_generate(dice),
        "one_pair": one_pair_generate(dice),
        "two_pair": two_pair_generate(dice),
        "three_of_a_kind": three_of_a_kind_generate(dice),
        "four_of_a_kind": four_of_a_kind_generate(dice),
        "full_house": full_house_generate(dice),
        "small_straight": small_straight_generate(dice),
        "large_straight": large_straight_generate(dice),
        "yezzi": yezzi_generate(dice),
        "chance": chance_generate(dice),
        }
        with open("game_data.json", "w") as f:
            json.dump(game_data, f, cls=CompactArrayEncoder, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error occurred: {e}")


def testing_count(combination_dict):
    s = 0
    for i in combination_dict:
        print(f"Score: {i}, Count: {len(combination_dict[i])}")
        if i != 0:
            s += len(combination_dict[i])
    print(f"s = {s}")


def testing_arrs(combination_dict):
    s = 0
    for i in combination_dict:
        print(f"Score: {i}, Arr: {combination_dict[i]}")


def main():
    dice = generate_dice()
    game_data_json(dice)
    one_dict = one_generate(dice)
    two_dict = two_generate(dice)
    three_dict = three_generate(dice)
    four_dict = four_generate(dice)
    five_dict = five_generate(dice)
    six_dict = six_generate(dice)
    one_pair_dict = one_pair_generate(dice)
    two_pair_dict = two_pair_generate(dice)
    three_of_a_kind_dict = three_of_a_kind_generate(dice)
    four_of_a_kind_dict = four_of_a_kind_generate(dice)
    full_house_dict = full_house_generate(dice)
    small_straight_dict = small_straight_generate(dice)
    large_straight_dict = large_straight_generate(dice)
    yezzi_dict = yezzi_generate(dice)
    chance_dict = chance_generate(dice)



    print("Test result")
    print('testing__count "one":')
    testing_count(one_dict)
    print('testing_count "two":')
    testing_count(two_dict)
    print('testing_count "three":')
    testing_count(three_dict)
    print('testing_count "four":')
    testing_count(four_dict)
    print('testing_count "five":')
    testing_count(five_dict)
    print('testing_count "six":')
    testing_count(six_dict)
    print('testing_count "one pair":')
    testing_count(one_pair_dict)
    print('testing_count "two pair":')
    testing_count(two_pair_dict)
    print('testing_count "three of a kind":')
    testing_count(three_of_a_kind_dict)
    print('testing_count "four of a kind":')
    testing_count(four_of_a_kind_dict)
    print('testing_count "full house":')
    testing_count(full_house_dict)
    print('testing_count "small straight":')
    testing_count(small_straight_dict)
    print('testing_count "large straight":')
    testing_count(large_straight_dict)
    print('testing_count "yezzi":')
    testing_count(yezzi_dict)
    print('testing_count "chance":')
    testing_count(chance_dict)


if __name__ == "__main__":
    main()
