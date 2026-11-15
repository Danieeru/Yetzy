"""
Yatzy - a dice game where players roll dice and try to achieve various combinations.
Each player gets three rolls per turn to achieve the best possible combination.
The game features a scoring system with bonus points for completing the upper section (64+ points).
"""
import combinations as comb_mod
import gameboard as board_mod
from dice import Dice

def get_valid_number() -> int:
    """Get and validate number of players (1-6) from user input."""
    while True:
        user_input = input("Number of players: ").strip()
        if not user_input:
            print("Error! Enter a non-empty value")
            continue
        if not user_input.isdigit():
            print(f"Error! '{user_input}' is not an integer!")
            continue
        number = int(user_input)
        if number not in range(1, 6):
            print("Error! Number players must be between 1 and 6.")
            continue
        return number
        

def one_turn(combinations: dict[str, list[str]], player: int) -> dict[str, int]:
    dice = Dice()
    for i in range(dice.count_roll):
        if i == 0:
            dice.roll_five_dices()
        else:
            reroll = dice.get_valid_dices()
            if reroll == dice.escape:
                break
            print(f"{i + 1}: Rerolling...")
            dice.reroll_few_dice()
        dice.print_five_dices()
        res = check_all_combinations(dice.dices)
        board_mod.print_comb(res, combinations, player)
    return res
            

def add_players(count_players: int) -> list[str]:
    """Get player names from user input and return list of player names."""
    players = []
    for i in range(count_players):
        while True:
            player_name = input(f"Player {i + 1} name: ")
            if player_name:
                if player_name not in players:
                    players.append(player_name)
                    break
                else:
                    print("Error! Name already exists!")
            else:
                print("Error! Name cannot be empty")
    return players


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
        "Yatzy": comb_mod.number_of_a_kind_check(dice, 5),
        "Chance": comb_mod.chance_check(dice)
    }
    res = dict(reversed(sorted(res.items(), key=lambda item: item[1])))
    return res


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
        elif com_input in ("yatzy", "y"):
            if combinations["Yatzy"][player] == "":
                combinations["Yatzy"][player] = res["Yatzy"]
                combinations["Total"][player] += res["Yatzy"]
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
        "Yatzy": [],
        "Chance": [],
        "Total": []
    }
    print("Welcome to Yatzy!")
    count_players = get_valid_number()
    players = add_players(count_players)
    block_nums = [0 for i in players]
    block_num_bool = [False for i in players]
    board_mod.create_start_table(combinations, players)
    print("Starting grid:")
    board_mod.draw_table(combinations, players)
    cells = board_mod.calc_cell(combinations)
    turn = 1
    while cells >= turn * count_players:
        print(f"Turn {turn}")
        for i, player in enumerate(players):
            input(f"{player}: Press Enter to roll the dice... ")
            res = one_turn(combinations, i)
            write_res_in_table(combinations, res, i, block_nums, block_num_bool)
            board_mod.draw_table(combinations, players)
        turn += 1


if __name__ == "__main__":
    main()
