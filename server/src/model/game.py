from config.constants import WOOD, WHITE, BLUE, SQUARE_SIZE
from .board import Board

class Game:
    def __init__(self, ):
        self._init()

    def _init(self):
        self.Board = Board()

    def change_turn(self, turn):
        if turn == str(WOOD):
            turn = str(WHITE)
        else:
            turn = str(WOOD)
        return turn

