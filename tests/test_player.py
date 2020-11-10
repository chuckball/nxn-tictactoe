import unittest

from game.board import Board
from game.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        player1 = Player(name="test1", symbol="o")
        player2 = Player(name="test2", symbol="x")
        self.board = Board(player1, player2, 3)

    def test_create_player(self):
        player3 = Player(name="test3", symbol="o")
        self.assertEqual(player3.name, "test3")
        self.assertEqual(player3.symbol, "o")

    def test_successful_search_and_input_symbol(self):
        self.board.current_player = self.board.player1
        self.board.grid_map = [['o', '2', 'o'],
                               ['x', '5', '6'],
                               ['x', '8', 'o']]
        self.board.player1._search_grid_and_input_symbol(6, self.board)
        new_grid_map = [['o', '2', 'o'],
                        ['x', '5', 'o'],
                        ['x', '8', 'o']]
        self.assertEqual(self.board.grid_map, new_grid_map)

    def test_fail_search_and_input_symbol(self):
        self.board.current_player = self.board.player1
        self.board.grid_map = [['o', '2', 'o'],
                               ['x', '5', '6'],
                               ['x', '8', 'o']]
        old_grid_map = self.board.grid_map
        self.board.current_player._search_grid_and_input_symbol(4, self.board)
        self.assertEqual(self.board.grid_map, old_grid_map)


if __name__ == '__main__':
    unittest.main()
