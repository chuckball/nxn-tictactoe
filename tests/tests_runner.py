# tests/tests_runner.py
import unittest
import sys
import os

# Hack for tests to work in terminal
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

# import your test modules

from tests import test_player, test_board, test_win_condition_logic, test_start_game

# initialize the test suite

loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(test_player))
suite.addTests(loader.loadTestsFromModule(test_board))
suite.addTests(loader.loadTestsFromModule(test_win_condition_logic))
suite.addTests(loader.loadTestsFromModule(test_start_game))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
