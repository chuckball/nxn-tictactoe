from .win_condition_logic import check_win_condition
from .helper import color_symbol
from .player import Player


class Board:
    def __init__(self, player1: Player, player2: Player, size: int = 3):
        """
        Create a new Board Object.

        :param player1: Player 1 details
        :param player2: Player 2 details
        :param size: Length of row/col of board
        """
        self.size: int = size
        self.player1: Player = player1
        self.player2: Player = player2
        self.max_moves: int = size * size
        self.grid_map: list = []
        self.current_player: Player = player1
        self._initialize_board(size)

    def _initialize_board(self, size: int):
        """Generate an empty game board."""
        n = 1
        for _ in range(size):
            col = []
            for _ in range(size):
                col.append(str(n))
                n += 1
            self.grid_map.append(col)

    def alternate_current_player(self):
        """Swap players turn every round."""
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def draw_board(self):
        """Draw game board into console, leaving out the last index so there isn't extra lines."""
        print('')
        for col in range(self.size):
            for row in range(self.size):
                if row == self.size - 1:
                    print(color_symbol(self.grid_map[col][row]).center(5))
                else:
                    print(color_symbol(self.grid_map[col][row]).center(5) + '|', end='')
            if col != self.size - 1:
                print('------' * self.size)
        print('')

    def play_game(self):
        for move_count in range(self.max_moves):
            if move_count % 2 == 0:
                self.player1.input_move(self)
            else:
                self.player2.input_move(self)
            if check_win_condition(self):
                self.draw_board()
                print("Congratulations {}! You have won.".format(self.current_player.name))
                break
            if move_count == self.max_moves - 1:
                self.draw_board()
                print("\nGame Over.")
                print("It's a Tie!")
