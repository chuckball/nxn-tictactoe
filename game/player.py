class Player:
    def __init__(self, name: str, symbol: str):
        """
        Create Player Object

        :param name: Player Name
        :param symbol: x / o
        """
        self.name: str = name
        self.symbol: str = symbol

    def input_move(self, board):
        while True:
            board.draw_board()
            try:
                player_move = int(
                    input(
                        self.name + ", pick a numbered grid to place an '{}':\n>> ".format(self.symbol)))
                if player_move < 1 or player_move > board.max_moves:
                    raise ValueError
            except ValueError:
                print("Input an integer between 1 and " + str(board.max_moves))
                continue

            if self._search_grid_and_input_symbol(player_move, board):
                break
            else:
                print("That grid is already filled.\nPlease pick another grid.")
                continue

    def _search_grid_and_input_symbol(self, input_value, board) -> bool:
        """Search of input on board"""
        # Find row position of input
        row = 0
        if input_value > board.size:
            for i in range(1, board.size):
                if (board.size * i) < input_value <= (board.size * (i + 1)):
                    row = i
        # Find col position of input
        if not (input_value % board.size) == 0:
            col = (input_value % board.size) - 1
        else:
            col = board.size - 1

        """Input symbol"""
        if board.grid_map[row][col] != 'x' and board.grid_map[row][col] != 'o':
            board.grid_map[row][col] = self.symbol
            return True
        else:
            return False