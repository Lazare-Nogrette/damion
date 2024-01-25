import pygame
from ..config.constants import BLACK, ROWS, WOOD, SQUARE_SIZE, COLS, WHITE
from .piece import Piece


class Board:
    def __init__(self, game_api):
        self.game_api = game_api
        self.board = []
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()

    def draw_squares(self, win):
        pass

    def move(self, piece, row, col):
        pass

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        pass

    def draw(self, win):
        self.draw_squares(win)
        for row in range( ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def remove(self, pieces):
        pass

    def winner(self):
        if self.red_left <= 0:
            return WHITE
        elif self.white_left <= 0:
            return WOOD

        return None

    # Method to get valid moves for a given piece
