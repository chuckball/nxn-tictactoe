import unittest

from game.board import Board
from game.win_condition_logic import check_win_condition
from game.player import Player


class TestWinConditionLogic(unittest.TestCase):
    def setUp(self):
        player1 = Player(name="test1", symbol="o")
        player2 = Player(name="test2", symbol="x")
        self.board = Board(player1, player2, 3)

    def test_diagonal_win_condition(self):
        self.board.grid_map = [['o', '2', '3'],
                               ['4', 'o', '6'],
                               ['7', '8', 'o']]
        self.assertEqual(check_win_condition(self.board), True)

        self.board.grid_map = [['o', '2', 'x'],
                               ['4', 'x', '6'],
                               ['x', '8', 'o']]
        self.assertEqual(check_win_condition(self.board), True)

    def test_vertical_win_condition(self):
        self.board.grid_map = [['o', '2', 'x'],
                               ['o', 'x', 'o'],
                               ['o', 'x', '9']]
        self.assertEqual(check_win_condition(self.board), True)

    def test_horizontal_win_condition(self):
        self.board.grid_map = [['o', '2', 'o'],
                               ['x', 'x', 'x'],
                               ['x', '8', 'o']]
        self.assertEqual(check_win_condition(self.board), True)

    def test_no_win_condition(self):
        self.board.grid_map = [['o', '2', 'o'],
                               ['x', '5', '6'],
                               ['x', '8', 'o']]
        self.assertEqual(check_win_condition(self.board), False)

        self.board.grid_map = [['o', '2', 'o'],
                               ['o', 'x', 'x'],
                               ['x', '8', 'o']]
        self.assertEqual(check_win_condition(self.board), False)

        self.board.grid_map = [['o', '2', 'o'],
                               ['x', '5', 'x'],
                               ['x', '8', 'o']]
        self.assertEqual(check_win_condition(self.board), False)


if __name__ == '__main__':
    unittest.main()
