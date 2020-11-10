import unittest
import sys
import os
from unittest import mock

from game.player import Player
from game.board import Board


class TestBoard(unittest.TestCase):
    def test_create_default_board(self):
        player1 = Player(name="test1", symbol="o")
        player2 = Player(name="test2", symbol="x")
        self.board = Board(player1, player2)
        self.assertEqual(self.board.grid_map, [['1', '2', '3'],
                                               ['4', '5', '6'],
                                               ['7', '8', '9']])

    def test_create_4x4_board(self):
        player1 = Player(name="test1", symbol="o")
        player2 = Player(name="test2", symbol="x")
        self.board = Board(player1, player2, 4)
        self.assertEqual(self.board.grid_map, [['1', '2', '3', '4'],
                                               ['5', '6', '7', '8'],
                                               ['9', '10', '11', '12'],
                                               ['13', '14', '15', '16']])

    def test_player_input(self):
        player1 = Player(name="test1", symbol="o")
        player2 = Player(name="test2", symbol="x")
        self.board = Board(player1, player2)

        with mock.patch('builtins.input', return_value="1"):
            player1.input_move(self.board)
        new_grid_map = [['o', '2', '3'],
                        ['4', '5', '6'],
                        ['7', '8', '9']]
        self.assertEqual(self.board.grid_map, new_grid_map)


if __name__ == '__main__':
    unittest.main()
