from ..config.constants import WOOD, WHITE, SQUARE_SIZE, GREY, CROWN
import pygame


class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, game_api, row, col, color):
        self.game_api = game_api
        self.row, self.col, self.color, self.king, self.x, self.y = row, col, color, False, 0, 0
        self.calc_pos()

    def calc_pos(self):
        pass

    def make_king(self):
        self.king = True

    def draw(self, win):
        pass

    def move(self, row, col):
        self.row, self.col = row, col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)
