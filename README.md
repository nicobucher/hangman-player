# hangman-player
A small python program that plays hangman

You can play yourself using the jar file "java -jar hangman.jar"

but you can also let python play "player.py java -jar hangman.jar".

The game is inspired by this assignment of Stanford University https://web.stanford.edu/class/archive/cs/cs106a/cs106a.1124/handouts/200%20Assignment%204.pdf

Possible solutions and benchmarks are discussed here
https://codegolf.stackexchange.com/questions/25496/write-a-hangman-solver

The current approach is to shuffle all characters of the english alphabet randomly in order to create a sequence of guess characters. This method can of course be optimized by introducing a more sophisticated decision tree or by ranking the guess characters after their likelihood of appearance in words.
