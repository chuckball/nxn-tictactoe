from game.player import Player
from game.board import Board

SYMBOLS = ['o', 'x']


def create_player_prompt(player_number: int) -> Player:
    while True:
        name = str(input("\nEnter name for Player {}: \n>> ".format(player_number)))
        if len(name) > 0:
            return Player(name=name, symbol="{}".format(SYMBOLS[player_number - 1]))


if __name__ == "__main__":
    player1 = create_player_prompt(1)
    player2 = create_player_prompt(2)
    default_size = 3

    size = input("\nEnter board size (default is 3): ")
    if len(size) < 1:
        size = 3
    else:
        try:
            size = int(size)
            if size < 0:
                raise ValueError()
        except ValueError:
            print("Invalid value entered. Defaulting to {}".format(default_size))
            size = default_size

    board = Board(size=size, player1=player1, player2=player2)
    board.play_game()
