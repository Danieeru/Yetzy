def number_check(dices: list[int], number: int) -> int:
    number_in_dices = dices.count(number)
    return number_in_dices * number


def number_of_a_kind_check(dices: list[int], number: int) -> int:
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

def two_pairs_check(dice: list[int]) -> int:
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
        elif count >= 2 and temp != -1:
            s = temp * 2 + num * 2
    return s


def full_house_check(dice: list[int]) -> int:
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


def small_straight_check(dice: list[int]) -> int:
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


def large_straight_check(dice: list[int]) -> int:
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


def chance_check(dices: list[int]) -> int:
    return sum(dices)