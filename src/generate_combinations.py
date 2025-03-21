import random
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

class SuperCompactEncoder(json.JSONEncoder):
    def encode(self, obj):
        if isinstance(obj, list) and all(isinstance(i, (int, float)) for i in obj):
            return f"[{','.join(map(str, obj))}]"
        return super().encode(obj)

def generate_dice():
    dice = list(itertools.product("123456", repeat=5))
    for i in range(len(dice)):
        dice[i] = [int(x) for x in dice[i]]
    return dice

def wrire_to_dict(dict_num, s, arr):
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
                wrire_to_dict(num_dict, 0, arr)
            if count >= temp_count != 0:
                wrire_to_dict(num_dict, num * temp_count, arr)
    return dict(sorted(num_dict.items()))


def two_generate(dice):
    num_dict = {}
    num = 2
    for arr in dice:
        count = arr.count(num)
        for temp_count in range(6):
            if count == temp_count == 0:
                wrire_to_dict(num_dict, 0, arr)
            if count >= temp_count != 0:
                wrire_to_dict(num_dict, num * temp_count, arr)
    return dict(sorted(num_dict.items()))


def three_generate(dice):
    num_dict = {}
    num = 3
    for arr in dice:
        count = arr.count(num)
        for temp_count in range(6):
            if count == temp_count == 0:
                wrire_to_dict(num_dict, 0, arr)
            if count >= temp_count != 0:
                wrire_to_dict(num_dict, num * temp_count, arr)
    return dict(sorted(num_dict.items()))


def four_generate(dice):
    num_dict = {}
    num = 4
    for arr in dice:
        count = arr.count(num)
        for temp_count in range(6):
            if count == temp_count == 0:
                wrire_to_dict(num_dict, 0, arr)
            if count >= temp_count != 0:
                wrire_to_dict(num_dict, num * temp_count, arr)
    return dict(sorted(num_dict.items()))


def five_generate(dice):
    num_dict = {}
    num = 5
    for arr in dice:
        count = arr.count(num)
        for temp_count in range(6):
            if count == temp_count == 0:
                wrire_to_dict(num_dict, 0, arr)
            if count >= temp_count != 0:
                wrire_to_dict(num_dict, num * temp_count, arr)
    return dict(sorted(num_dict.items()))


def six_generate(dice):
    num_dict = {}
    num = 6
    for arr in dice:
        count = arr.count(num)
        for temp_count in range(6):
            if count == temp_count == 0:
                wrire_to_dict(num_dict, 0, arr)
            if count >= temp_count != 0:
                wrire_to_dict(num_dict, num * temp_count, arr)
    return dict(sorted(num_dict.items()))


def one_pair_generate(dice):
    one_pair_dict = {}
    for arr in dice:
        counts = {}
        for num in arr:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        for num, count in counts.items():
            if count >= 2:
                sum_pair = num * 2
                if sum_pair not in one_pair_dict:
                    one_pair_dict[sum_pair] = []
                one_pair_dict[sum_pair].append(arr)
    return dict(sorted(one_pair_dict.items()))
def two_pair_generate(dice):
    two_pair_dict = {}
    for arr in dice:
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
                sum_pair = temp * 2 + num * 2
                if sum_pair not in two_pair_dict:
                    two_pair_dict[sum_pair] = []
                two_pair_dict[sum_pair].append(arr)
                temp = -1
    return dict(sorted(two_pair_dict.items()))
def three_of_a_kind_generate(dice):
    toak_dic = {}
    for arr in dice:
        counts = {}
        for num in arr:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        for num, count in counts.items():
            if count >= 3:
                sum_toak = num * 3
                if sum_toak not in toak_dic:
                    toak_dic[sum_toak] = []
                toak_dic[sum_toak].append(arr)
    return dict(sorted(toak_dic.items()))           
def four_of_a_kind_generate(dice):
    foak_dic = {}
    for arr in dice:
        counts = {}
        for num in arr:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        for num, count in counts.items():
            if count >= 4:
                sum_foak = num * 4
                if sum_foak not in foak_dic:
                    foak_dic[sum_foak] = []
                foak_dic[sum_foak].append(arr)
    return dict(sorted(foak_dic.items()))
def full_house_generate(dice):
    # нету нормальной обрабоки случая 4 + 1
    fh_dict = {}
    for arr in dice:
        counts = {}
        for num in arr:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        if len(counts) == 2: # сюда заходят комбинации 4 + 1, нужен апргейд
            sum_fh = 0
            for num, count in counts.items():
                if count == 2 or count == 3:
                    sum_fh += num * count
            if sum_fh != 0:
                if sum_fh not in fh_dict:
                    fh_dict[sum_fh] = []
                fh_dict[sum_fh].append(arr)
    return dict(sorted(fh_dict.items()))      

def small_straight_generate(dice):
    s_street_dict = {}
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
                total = sum(subarray)
                if total not in s_street_dict:
                    s_street_dict[total] = []
                s_street_dict[total].append(arr)
                found = True
        if not found:
            total = 0
            if total not in s_street_dict:
                s_street_dict[total] = []
            s_street_dict[total].append(arr)
    return dict(sorted(s_street_dict.items()))  


def large_straight_generate(dice):
    b_street = {}
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
                total = sum(subarray)
                if total not in b_street:
                    b_street[total] = []
                b_street[total].append(arr)
                found = True
        if not found:
            total = 0
            if total not in b_street:
                b_street[total] = []
            b_street[total].append(arr)
    return dict(sorted(b_street.items()))


def yezzi_generate(dice):
    yezzi_dic = {}
    for arr in dice:
        counts = {}
        for num in arr:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        for num, count in counts.items():
            if count == 5:
                sum_yezzi = num *5
                if sum_yezzi not in yezzi_dic:
                    yezzi_dic[sum_yezzi] = []
                yezzi_dic[sum_yezzi].append(arr)
    return dict(sorted(yezzi_dic.items()))


def chance_generate(dice):
    dic_chance = {}
    for arr in dice:
        s_1 = sum(arr)
        if s_1 not in dic_chance:
            dic_chance[s_1] = []
        dic_chance[s_1].append(arr)
    return dict(sorted(dic_chance.items()))


def game_data_jsonl(dice):
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
        s += len(combination_dict[i])
    # print(f"s = {s}")


def testing_arrs(combination_dict):
    s = 0
    for i in combination_dict:
        print(f"Score: {i}, Arr: {combination_dict[i]}")


def main():
    dice = generate_dice()
    # game_data_json(dice)
    game_data_jsonl(dice)
    # one_dict = one_generate(dice)
    # two_dict = two_generate(dice)
    # three_dict = three_generate(dice)
    # four_dict = four_generate(dice)
    # five_dict = five_generate(dice)
    # six_dict = six_generate(dice)
    # one_pair_dict = one_pair_generate(dice)
    # two_pair_dict = two_pair_generate(dice)
    # three_of_a_kind_dict = three_of_a_kind_generate(dice)
    # four_of_a_kind_dict = four_of_a_kind_generate(dice)
    # full_house_dict = full_house_generate(dice)
    # small_straight_dict = small_straight_generate(dice)
    # large_straight_dict = large_straight_generate(dice)
    # yezzi_dict = yezzi_generate(dice)
    # chance_dict = chance_generate(dice)



    # print("Test result")
    # print('testing__count "one":')
    # testing_count(one_dict)
    # print('testing_count "two":')
    # testing_count(two_dict)
    # print('testing_count "three":')
    # testing_count(three_dict)
    # print('testing_count "four":')
    # testing_count(four_dict)
    # print('testing_count "five":')
    # testing_count(five_dict)
    # print('testing_count "six":')
    # testing_count(six_dict)
    # print('testing_count "one pair":')
    # testing_count(one_pair_dict)
    # print('testing_count "two pair":')
    # testing_count(two_pair_dict)
    # print('testing_count "three of a kind":')
    # testing_count(three_of_a_kind_dict)
    # print('testing_count "four of a kind":')
    # testing_count(four_of_a_kind_dict)
    # print('testing_count "full house":')
    # testing_count(full_house_dict)
    # print('testing_count "small straight":')
    # testing_count(small_straight_dict)
    # print('testing_count "large straight":')
    # testing_count(large_straight_dict)
    # print('testing_count "yezzi":')
    # testing_count(yezzi_dict)
    # print('testing_count "chance":')
    # testing_count(chance_dict)



    # chance_dict = chance_generate(dice)
    # for i in one_dict:
    #     print(f"One: {i}, Count: {one_dict[i]}")
    #     print("=========================")
    # for i in two_dict:
    #     print(f"Two: {i}, Count: {two_dict[i]}")
    #     print("=========================")
    # for i in three_dict:
    #     print(f"Three: {i}, Count: {three_dict[i]}")
    #     print("=========================")
    # for i in four_dict:
    #     print(f"Four: {i}, Count: {four_dict[i]}")
    #     print("=========================")
    # for i in five_dict:
    #     print(f"Five: {i}, Count: {five_dict[i]}")
    #     print("=========================")
    # for i in six_dict:
    #     print(f"Six: {i}, Count: {six_dict[i]}")
    #     print("=========================")
    # for i in one_pair_dict:
    #     print(f"One: {i}, Count: {one_pair_dict[i]}")
    #     print("=========================")
    # for i in two_pair_dict:
    #     print(f"Two: {i}, Count: {two_pair_dict[i]}")
    #     print("=========================")
    # for i in three_of_a_kind_dict:
    #     print(f"Three of a kind: {i}, Count: {three_of_a_kind_dict[i]}")
    #     print("=========================")
    # for i in one_pair_dict:
    #     print(f"{i}: {one_pair_dict[i]} ")
    # print("=========================")
    # for i in two_pair_dict:
    #     print(f"{i}: {two_pair_dict[i]} ")
    # for i in three_of_a_kind_dict:
    #     print(f"{i}: {three_of_a_kind_dict[i]} ")
    # print("=========================")





if __name__ == "__main__":
    main()