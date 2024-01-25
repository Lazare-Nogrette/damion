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
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, WOOD, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        is_game_config = self.game_api.init_game()
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        # piece = Piece(self.game_api, row, col, WHITE)
                        # print(f'row < 3: {piece}')
                        self.board[row].append(Piece(self.game_api, row, col, WHITE))
                    elif row > 4:
                        # piece = Piece(self.game_api, row, col, WOOD)
                        # print(f'row > 4: {piece}')
                        self.board[row].append(Piece(self.game_api, row, col, WOOD))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_squares(win)
        for row in range( ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def remove(self, pieces):
        pass

        # print(f'Available Pieces to remove: {pieces}')

    def winner(self):
        if self.red_left <= 0:
            return WHITE
        elif self.white_left <= 0:
            return WOOD

        return None

    # Method to get valid moves for a given piece
    def get_valid_moves(self, piece):
        pass

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        pass

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        pass
