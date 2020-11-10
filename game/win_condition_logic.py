def _check_horizontal_win_condition(board) -> bool:
    for col in range(board.size):
        for row in range(board.size):
            # Skip checking last 2 row edge case
            if row != (board.size - 1) and row != (board.size - 2):
                # Check rightwards if 3 symbols match from current grid
                if board.grid_map[col][row] == board.grid_map[col][row + 1] == board.grid_map[col][row + 2]:
                    return True
    return False


def _check_vertical_win_condition(board) -> bool:
    for col in range(board.size):
        # Skip checking last 2 col edge case
        if col != (board.size - 1) and col != (board.size - 2):
            for row in range(board.size):
                # Check downwards if 3 symbols match from current grid
                if board.grid_map[col][row] == board.grid_map[col + 1][row] == board.grid_map[col + 2][row]:
                    return True
    return False


def _check_diagonal_win_condition(board) -> bool:
    for col in range(board.size):
        # Skip checking last/first 1 row/col
        if col != 0 and col != (board.size - 1):
            for row in range(board.size):
                if row != 0 and row != (board.size - 1):
                    # 1. Check diagonally from upper left grid of current grid towards lower right grid
                    # 2. Check diagonally from upper right grid of current grid towards lower left grid
                    if board.grid_map[col][row] == board.grid_map[col - 1][row - 1] == board.grid_map[col + 1][row + 1] \
                            or board.grid_map[col][row] == \
                            board.grid_map[col - 1][row + 1] == \
                            board.grid_map[col + 1][row - 1]:
                        return True
    return False


def check_win_condition(board) -> bool:
    """
    Check for win conditions to end the game.

    1: Check for vertical win condition
    2: Check for horizontal win condition
    3: Check for diagonal win condition

    If not, change player turn
    """
    if _check_vertical_win_condition(board) or _check_horizontal_win_condition(board) or _check_diagonal_win_condition(
            board):
        return True
    else:
        board.alternate_current_player()
    return False
