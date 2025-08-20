"""
Module for managing the game board and table operations in Yezzi game.
Contains functions for creating, displaying and updating the game table.
"""

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
    for comb, player in combinations.items():
        print("+" + "-" * 17 + ("+" + "-" * (max_name + 4)) * count_players + "+")
        print(f"| {comb:^15} |", end="")
        for i in range(count_players):
            print(f" {player[i]:^{max_name + 2}} |",end="")
        print()
        if comb == "Total":
            (print("+" + "-" * 17 + ("+" + "-" * (max_name + 4)) * count_players + "+"))    


def print_comb(res: dict[str, int], combinations: dict[str, list[str]], player: int) -> None:
    """Print available combinations and their scores for current player."""
    for comb, r in res.items():
        if r != 0 and combinations[comb][player] == "":
            print(f"| {comb}: {r} ", end="")
        else:
            continue
    print("|", end="\n")


def calc_cell(combinations: dict[str, list[str]]) -> int:
    """Calculate total number of cells in the game table."""
    s = 0
    for comb, scores in combinations.items():
        if comb in ("64/35", "Total"):
            continue
        s += len(scores)
    return s
