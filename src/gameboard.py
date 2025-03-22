import sys
import time

combinations = {
    "64/35": ["Danya"],
    "1": [1],
    "2": [1],
    "3": [1],
    "4": [1],
    "5": [1],
    "6": [1],
    "One Pair": [1],
    "Two Pair": [1],
    "Three of a Kind": [1],
    "Four of a Kind": [1],
    "Full House": [1],
    "Small straight": [1],
    "Large straight": [1],
    "Yezzi": [1],
    "Chance": [1],
    "Result": [1]
}


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
    players = add_players()
    create_start_table(combinations_ru, players)
    draw_table(combinations_ru, players)
    time.sleep(3)
    print()


if __name__ == "__main__":
    main()

