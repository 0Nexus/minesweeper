from game import Game
from board import Board
size = (9, 9)
prob = 0.2
board = Board(size, prob)
screenSize = (800, 600)
game = Game(board, screenSize)
game.run()