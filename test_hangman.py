'''
Created on 15.06.2018

@author: nicobucher
'''
from hangman import hangman
import pytest

@pytest.fixture()
def hangman_game():
    game = hangman.HangmanGame('test')
    return game

def test_init(hangman_game):
    assert hangman_game._chars != 'abcdefghijklmnopqrstuvwxyz'

# '____' and 'BBBBBB' are a problem, the length of the searched word should not change.
# Also a previously identified character should not change.
# This is not yet detected by the current implementation
@pytest.mark.parametrize('answer', ['____', '_____', 'AA_AA', 'BBBBBB'])
def test_answer_correct(hangman_game, answer):
    hangman_game._last_answer = answer
    assert hangman_game.check_answer('__T__')
    
def test_answer_incorrect(hangman_game):
    hangman_game._last_answer = '__T__'
    assert hangman_game.check_answer('__T__') == False