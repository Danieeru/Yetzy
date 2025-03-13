import random
import itertools
import json

# Можно использовать Counter из collections для подсчета уникальных символов в массиве

def generate_full_houses_2():
    dic_fh = {}
    dice = list(itertools.combinations([1, 2, 3, 4, 5, 6], 2))
    for i in range(len(dice)):
        temp_1 = [dice[i][0] for j in range(3)]
        temp_1.extend([dice[i][1] for j in range(2)])
        temp_2 = [dice[i][0] for j in range(2)]
        temp_2.extend(dice[i][1] for j in range(3))
        s_1 = sum(temp_1)
        s_2 = sum(temp_2)
        if s_1 not in dic_fh:
            dic_fh[s_1] = []
        dic_fh[s_1].append(temp_1)
        if s_2 not in dic_fh:
            dic_fh[s_2] = []
        dic_fh[s_2].append(temp_2)
    return dict(sorted(dic_fh.items()))
    

def generate_two_pairs():
    dic_tp = {}
    dice = list(itertools.combinations([1, 2, 3, 4, 5, 6], 2))
    for i in range(len(dice)):
        temp_1 = [dice[i][0] for j in range(2)]
        temp_1.extend([dice[i][1] for j in range(2)])
        s_1 = sum(temp_1)
        if s_1 not in dic_tp:
            dic_tp[s_1] = []
        dic_tp[s_1].append(temp_1)
    return dict(sorted(dic_tp.items()))



def generate_dice():
    dice = list(itertools.product("123456", repeat=5))
    for i in range(len(dice)):
        dice[i] = [int(x) for x in dice[i]]
    return dice

def one_generate(dice):
    dice = generate_dice()
    one_dict = {}
    for i in range(len(dice)):
        s_1 = sum(x for x in dice[i] if x == 1)
        if s_1 not in one_dict:
            one_dict[s_1] = []
        one_dict[s_1].append(dice[i])
    return dict(sorted(one_dict.items()))
def two_generate(dice):
    one_dict = {}
    for i in range(len(dice)):
        s_1 = sum(x for x in dice[i] if x == 2)
        if s_1 not in one_dict:
            one_dict[s_1] = []
        one_dict[s_1].append(dice[i])
    return dict(sorted(one_dict.items()))
def three_generate(dice):
    one_dict = {}
    for i in range(len(dice)):
        s_1 = sum(x for x in dice[i] if x == 3)
        if s_1 not in one_dict:
            one_dict[s_1] = []
        one_dict[s_1].append(dice[i])
    return dict(sorted(one_dict.items()))
def four_generate(dice):
    one_dict = {}
    for i in range(len(dice)):
        s_1 = sum(x for x in dice[i] if x == 4)
        if s_1 not in one_dict:
            one_dict[s_1] = []
        one_dict[s_1].append(dice[i])
    return dict(sorted(one_dict.items()))
def five_generate(dice):
    one_dict = {}
    for i in range(len(dice)):
        s_1 = sum(x for x in dice[i] if x == 5)
        if s_1 not in one_dict:
            one_dict[s_1] = []
        one_dict[s_1].append(dice[i])
    return dict(sorted(one_dict.items()))
def six_generate(dice):
    one_dict = {}
    for i in range(len(dice)):
        s_1 = sum(x for x in dice[i] if x == 6)
        if s_1 not in one_dict:
            one_dict[s_1] = []
        one_dict[s_1].append(dice[i])
    return dict(sorted(one_dict.items()))
def one_pair_generate(dice):
    one_pair_dict = {}
    for i in range(len(dice)):
        counts = {}
        for num in dice[i]:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        for num, count in counts.items():
            if count >= 2:
                sum_pair = num * 2
                if sum_pair not in one_pair_dict:
                    one_pair_dict[sum_pair] = []
                one_pair_dict[sum_pair].append(dice[i])
    return dict(sorted(one_pair_dict.items()))


def two_pair_generate(dice):
    two_pair_dict = {}
    for i in range(len(dice)):
        counts = {}
        for num in dice[i]:
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
                two_pair_dict[sum_pair].append(dice[i])
                temp = -1
    return dict(sorted(two_pair_dict.items()))

def three_of_a_kind_generate(dice):
    toak_dic = {}
    for i in range(len(dice)):
        counts = {}
        for num in dice[i]:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        for num, count in counts.items():
            if count >= 3:
                sum_toak = num * 3
                if sum_toak not in toak_dic:
                    toak_dic[sum_toak] = []
                toak_dic[sum_toak].append(dice[i])
    return dict(sorted(toak_dic.items()))

            
def four_of_a_kind_generate(dice):
    foak_dic = {}
    for i in range(len(dice)):
        counts = {}
        for num in dice[i]:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        for num, count in counts.items():
            if count >= 4:
                sum_foak = num * 4
                if sum_foak not in foak_dic:
                    foak_dic[sum_foak] = []
                foak_dic[sum_foak].append(dice[i])
    return dict(sorted(foak_dic.items()))


def full_house_generate(dice):
    # нету нормальной обрабоки случая 4 + 1
    fh_dict = {}
    for i in range(len(dice)):
        counts = {}
        for num in dice[i]:
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
                fh_dict[sum_fh].append(dice[i])
    return dict(sorted(fh_dict.items()))

        
def small_straight_generate(dice):
    pass
def large_straight_generate(dice):
    pass
def yezzi_generate(dice):
    yezzi_dic = {}
    for i in range(len(dice)):
        counts = {}
        for num in dice[i]:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        for num, count in counts.items():
            if count == 5:
                sum_yezzi = num *5
                if sum_yezzi not in yezzi_dic:
                    yezzi_dic[sum_yezzi] = []
                yezzi_dic[sum_yezzi].append(dice[i])
    return dict(sorted(yezzi_dic.items()))

def chance_generate():
    dic_chance = {}
    dice = list(itertools.combinations_with_replacement([1, 2, 3, 4, 5, 6], 5))
    for i in range(len(dice)):
        s_1 = sum(dice[i])
        if s_1 not in dic_chance:
            dic_chance[s_1] = []
        dic_chance[s_1].append(dice[i])
    return dict(sorted(dic_chance.items()))


def main():
    dice = generate_dice()
    print(len(dice))
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
    # small_straight_dict = small_straight_generate(dice)
    # large_straight_dict = large_straight_generate(dice)
    yezzi_dict = yezzi_generate(dice)
    for i in yezzi_dict:
        print(f"Full House: {i}, Count: {len(yezzi_dict[i])}")
        print("=========================")

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