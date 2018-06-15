#!/usr/bin/env python3
''' Created on 15.06.2018

    @author: nicobucher
    
    A player for the hangman game 

    As proposed here:
    https://techdevguide.withgoogle.com/paths/foundational/hangman-solutions-open-source-answer/#!
    and here
    https://codegolf.stackexchange.com/questions/25496/write-a-hangman-solver 
'''
from hangman import hangman

def main(arg):
    game = hangman.HangmanGame(arg)
    game.play()
    pass

if __name__ == "__main__":
    import sys
    try:
        arg = sys.argv[1:]
    except Exception as e:
        print('Missing argument path of game executable')
        exit()
    main(arg)
