'''
Created on 15.06.2018

@author: nicobucher
'''
import subprocess
import random
from time import sleep

class HangmanGame(object):
    ''' Hangman Game Class
    
    This class playes the hangman game provided by an executable as
    a subprocess. Communicates via stdin and stdout.
    '''
    _chars = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self, executable):
        '''
        Constructor
        '''
        self._last_answer = ''
        self._chars = ''.join(random.sample(self._chars,len(self._chars)))
        self._executable = " ".join(executable )
        self._proc = subprocess.Popen(self._executable, 
                                         universal_newlines=True, 
                                         shell=True, 
                                         stdin=subprocess.PIPE, 
                                         stdout=subprocess.PIPE, 
                                         stderr=subprocess.STDOUT, 
                                         encoding="utf-8")
        
        
    def guess(self, char):
        self.poll_process(self._proc)
        for line in iter(self._proc.stdout.readline, 'Guess: \n'):
            print(line)
        self._proc.stdin.write(char + '\n')
        self._proc.stdin.flush()
        line = self._proc.stdout.readline()
        print(line)
        if '_' in line:
            self.check_answer(line)
        elif len(line) == len(self._last_answer):
            return True
        else:
            self.poll_process(self._proc)
            return False
        
    def check_answer(self, answer):
        if answer == self._last_answer:
            return False
        else:
            self._last_answer = answer
            return True
        
    def play(self):
        guesses = list(self._chars)
        for char in guesses:
            try:
                if self.guess(char) is True:
                    break
            except Exception as e:
                print(e)
                exit()
        else:
            print('Game Over')
        print('We won')
        
    def poll_process(self, process):
        process.poll()
        sleep(1)
        ret = process.returncode
        if ret is not None:
            raise Exception('Game exited')
    
    def __repr__(self):
        return "HangmanGame: executable -> " + self._executable
