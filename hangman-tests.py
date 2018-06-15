'''
Created on 15.06.2018

@author: nicobucher
'''
import unittest
from hangman import hangman
from wheel.signatures import assertTrue


class TestHangman(unittest.TestCase):


    def test_init(self):
        game = hangman.HangmanGame('test')
        self.assertEqual(game._chars,'abcdefghijklmnopqrstuvwxyz')

    def test_answer_correct(self):
        game = hangman.HangmanGame('test')
        game._last_answer = '_____'
        self.assertTrue(game.check_answer('__T__'))
        
    def test_answer_incorrect(self):
        game = hangman.HangmanGame('test')
        game._last_answer = '__T__'
        self.assertFalse(game.check_answer('__T__'))
        
        
if __name__ == '__main__':
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()