"""
Yezzi - a dice game where players roll dice and try to achieve various combinations.
Each player gets three rolls per turn to achieve the best possible combination.
The game features a scoring system with bonus points for completing the upper section (64+ points).
"""
import random
import sys
from . import combinations as comb_mod


def get_valid_number() -> int:
    """Get and validate number of players (1-6) from user input."""
    while True:
        user_input = input("Number of players: ").strip()
        if not user_input:
            print("Error! Enter a non-empty value")
            continue
        try:
            number = int(user_input)
            if 1 <= number <= 6:
                return number
            print("Error! Number of players must be between 1 and 6")
        except ValueError:
            print(f"Error! '{user_input}' is not an integer")


def get_valid_array(dice: list[int]) -> list[int]:
    """Get and validate dice to keep from user input, returns list of dice numbers or 'q' to quit."""
    count_res = {}
    for num in dice:
        if num in count_res:
            count_res[num] += 1
        else:
            count_res[num] = 1
    while True:
        user_input = input("Keep: ")
        if user_input == "q":
            return "q"
        if not user_input:
            return []
        elements = list(user_input.replace(" ", ""))
        if len(elements) > 5:
            print("Error! Cannot keep more than five dice")
            continue
        val_nums = []
        val_nums_count = {}
        for elem in elements:
            try:
                number = int(elem)
                if 1 <= number <= 6:
                    val_nums.append(number)
                else:
                    print("Error! Number must be between 1 and 6")
                    break
            except ValueError:
                print("Error! Must be integers only")
                break
        else:
            for num in val_nums:
                if num in val_nums_count:
                    val_nums_count[num] += 1
                else:
                    val_nums_count[num] = 1
            for num, count in val_nums_count.items():
                if num not in count_res or count > count_res[num]:
                    print("Error! No such dice!")
                    break
            else:
                return val_nums


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


def one_turn(combinations: dict[str, list[str]], player: int) -> dict[str, int]:
    """Execute one player's turn: roll dice, show combinations, allow rerolls."""
    print("Rolling five dice...")
    dice = roll_five_dice()
    print_five_dice(dice)
    res = check_all_combinations(dice)
    print_comb(res, combinations, player)
    for i in range(2):
        print(f"{i + 1}: Rerolling...")
        reroll = get_valid_array(dice)
        reroll_few_dice(dice, reroll)
        print(f"Updated dice: {dice}")
        print_five_dice(dice)
        res = check_all_combinations(dice)
        print_comb(res, combinations, player)
    return res


def add_players(count_players: int) -> list[str]:
    """Get player names from user input and return list of player names."""
    players = []
    for i in range(count_players):
        while True:
            player_name = input(f"Player {i + 1} name: ")
            if not player_name:
                print("Error! Name cannot be empty")
            else:
                players.append(player_name)
                break
    return players


def create_start_table(combinations: dict[str, list[str]], players: list[str]) -> None:
    """Initialize game table with player names and empty scores."""
    count_players = len(players)
    for comb, player in combinations.items():
        for i in range(count_players):
            if comb == "64/35":
                player.append(players[i])
            elif comb == "Total":
                player.append(0)
            else:
                player.append("")


def draw_table(combinations: dict[str, list[str]], players: list[str]) -> None:
    """Display current game state in a formatted table."""
    count_players = len(players)
    max_name = max(len(name) for name in players)
    sys.stdout.write("\033[F" * (count_players - 25))
    for comb, player in combinations.items():
        print("+" + "-" * 17 + ("+" + "-" * (max_name + 4)) * count_players + "+")
        print(f"| {comb:^15} |", end="")
        for i in range(count_players):
            print(f" {player[i]:^{max_name + 2}} |",end="")
        print()


def check_all_combinations(dice: list[int]) -> dict[str, int]:
    """Calculate scores for all possible combinations with given dice."""
    res = {
        "Ones": comb_mod.number_check(dice, 1),
        "Twos": comb_mod.number_check(dice, 2),
        "Threes": comb_mod.number_check(dice, 3),
        "Fours": comb_mod.number_check(dice, 4),
        "Fives": comb_mod.number_check(dice, 5),
        "Sixes": comb_mod.number_check(dice, 6),
        "Pair": comb_mod.number_of_a_kind_check(dice, 2),
        "Two Pairs": comb_mod.two_pairs_check(dice),
        "Three of a Kind": comb_mod.number_of_a_kind_check(dice, 3),
        "Four of a Kind": comb_mod.number_of_a_kind_check(dice, 4),
        "Full House": comb_mod.full_house_check(dice),
        "Small Straight": comb_mod.small_straight_check(dice),
        "Large Straight": comb_mod.large_straight_check(dice),
        "Yezzi": comb_mod.number_of_a_kind_check(dice, 5),
        "Chance": comb_mod.chance_check(dice)
    }
    res = dict(reversed(sorted(res.items(), key=lambda item: item[1])))
    return res

def print_comb(res: dict[str, int], combinations: dict[str, list[str]], player: int) -> None:
    """Print available combinations and their scores for current player."""
    for comb, r in res.items():
        if r != 0 and combinations[comb][player] == "":
            print(f"| {comb}: {r} ", end="")
        else:
            continue
    print("|", end="\n")


def write_res_in_table(combinations: dict[str, list[str]], res: dict[str, int],
                    player: int, block_nums: list[int], block_num_bool: list[bool]) -> None:
    """Process player's choice of combination and update scores."""
    while True:
        com_input = input("Record: ").lower().strip().replace(" ", "")
        if com_input in ("1", "ones"):
            if combinations["Ones"][player] == "":
                combinations["Ones"][player] = res["Ones"]
                combinations["Total"][player] += res["Ones"]
                block_nums[player] += res["Ones"]
            else:
                print("Error! Result already recorded.")
                continue
        elif com_input in ("2", "twos"):
            if combinations["Twos"][player] == "":
                combinations["Twos"][player] = res["Twos"]
                combinations["Total"][player] += res["Twos"]
                block_nums[player] += res["Twos"]
            else:
                print("Error! Result already recorded.")
                continue
        elif com_input in ("3", "threes"):
            if combinations["Threes"][player] == "":
                combinations["Threes"][player] = res["Threes"]
                combinations["Total"][player] += res["Threes"]
                block_nums[player] += res["Threes"]
            else:
                print("Error! Result already recorded.")
                continue
        elif com_input in ("4", "fours"):
            if combinations["Fours"][player] == "":
                combinations["Fours"][player] = res["Fours"]
                combinations["Total"][player] += res["Fours"]
                block_nums[player] += res["Fours"]
            else:
                print("Error! Result already recorded.")
                continue
        elif com_input in ("5", "fives"):
            if combinations["Fives"][player] == "":
                combinations["Fives"][player] = res["Fives"]
                combinations["Total"][player] += res["Fives"]
                block_nums[player] += res["Fives"]
            else:
                print("Error! Result already recorded.")
                continue
        elif com_input in ("6", "sixes"):
            if combinations["Sixes"][player] == "":
                combinations["Sixes"][player] = res["Sixes"]
                combinations["Total"][player] += res["Sixes"]
                block_nums[player] += res["Sixes"]
            else:
                print("Error! Result already recorded.")
                continue
        elif com_input in ("pair", "p"):
            if combinations["Pair"][player] == "":
                combinations["Pair"][player] = res["Pair"]
                combinations["Total"][player] += res["Pair"]
            else:
                print("Error! Result already recorded.")
                continue
        elif com_input in ("twopairs", "tp"):
            if combinations["Two Pairs"][player] == "":
                combinations["Two Pairs"][player] = res["Two Pairs"]
                combinations["Total"][player] += res["Two Pairs"]
            else:
                print("Error! Result already recorded.")
                continue
        elif com_input in ("threeofakind", "t"):
            if combinations["Three of a Kind"][player] == "":
                combinations["Three of a Kind"][player] = res["Three of a Kind"]
                combinations["Total"][player] += res["Three of a Kind"]
            else:
                print("Error! Result already recorded.")
                continue
        elif com_input in ("fourofakind", "f"):
            if combinations["Four of a Kind"][player] == "":
                combinations["Four of a Kind"][player] = res["Four of a Kind"]
                combinations["Total"][player] += res["Four of a Kind"]
            else:
                print("Error! Result already recorded.")
                continue
        elif com_input in ("fullhouse", "fh"):
            if combinations["Full House"][player] == "":
                combinations["Full House"][player] = res["Full House"]
                combinations["Total"][player] += res["Full House"]
            else:
                print("Error! Result already recorded.")
                continue
        elif com_input in ("smallstraight", "ss"):
            if combinations["Small Straight"][player] == "":
                combinations["Small Straight"][player] = res["Small Straight"]
                combinations["Total"][player] += res["Small Straight"]
            else:
                print("Error! Result already recorded.")
                continue
        elif com_input in ("largestraight", "ls"):
            if combinations["Large Straight"][player] == "":
                combinations["Large Straight"][player] = res["Large Straight"]
                combinations["Total"][player] += res["Large Straight"]
            else:
                print("Error! Result already recorded.")
                continue
        elif com_input in ("yezzi", "y"):
            if combinations["Yezzi"][player] == "":
                combinations["Yezzi"][player] = res["Yezzi"]
                combinations["Total"][player] += res["Yezzi"]
            else:
                print("Error! Result already recorded.")
                continue
        elif com_input in ("chance", "c"):
            if combinations["Chance"][player] == "":
                combinations["Chance"][player] = res["Chance"]
                combinations["Total"][player] += res["Chance"]
            else:
                print("Error! Result already recorded.")
                continue
        else:
            print("Error! No such command!")
            continue
        break
    if block_nums[player] >= 64 and block_num_bool[player] is False:
        block_num_bool[player] = True
        combinations["Total"][player] += 35
        print("BLOCK COMPLETED! +35")


def calc_cell(combinations: dict[str, list[str]]) -> int:
    """Calculate total number of cells in the game table."""
    s = 0
    for comb, scores in combinations.items():
        if comb in ("64/35", "Total"):
            continue
        s += len(scores)
    return s


def main() -> None:
    """Main game loop: initialize game, handle turns until completion."""
    combinations = {
        "64/35": [],
        "Ones": [],
        "Twos": [],
        "Threes": [],
        "Fours": [],
        "Fives": [],
        "Sixes": [],
        "Pair": [],
        "Two Pairs": [],
        "Three of a Kind": [],
        "Four of a Kind": [],
        "Full House": [],
        "Small Straight": [],
        "Large Straight": [],
        "Yezzi": [],
        "Chance": [],
        "Total": []
    }
    print("Welcome to Yezzi!")
    count_players = get_valid_number()
    players = add_players(count_players)
    block_nums = [0 for i in players]
    block_num_bool = [False for i in players]
    create_start_table(combinations, players)
    print("Starting grid:")
    draw_table(combinations, players)
    cells = calc_cell(combinations)
    turn = 1
    while cells >= turn * count_players:
        print(f"Turn {turn}")
        for i, player in enumerate(players):
            print(f"{player}:")
            res = one_turn(combinations, i)
            write_res_in_table(combinations, res, i, block_nums, block_num_bool)
            draw_table(combinations, players)
        turn += 1


if __name__ == "__main__":
    main()
