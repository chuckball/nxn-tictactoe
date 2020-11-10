import unittest
from unittest import mock

from start_game import create_player_prompt


class TestStartGame(unittest.TestCase):
    def test_create_player_prompt(self):
        with mock.patch('builtins.input', return_value='test1'):
            player1 = create_player_prompt(1)
            self.assertEqual(player1.symbol, 'o')
            self.assertEqual(player1.name, 'test1')
        with mock.patch('builtins.input', return_value='test2'):
            player2 = create_player_prompt(2)
            self.assertEqual(player2.symbol, 'x')
            self.assertEqual(player2.name, 'test2')


if __name__ == '__main__':
    unittest.main()
