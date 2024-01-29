from config.constants import ROWS, WOOD, COLS, WHITE, SQUARE_SIZE
from .piece import Piece


# Define the Board class
class Board:
    # Constructor method, initializes the board and game state
    def __init__(self):
        self.board = []  # 2D list to represent the game board
        self.red_left = self.white_left = 12  # Number of red and white pieces initially
        self.Piece = Piece()
        self.rows = ROWS
        self.cols = COLS
        self.window_size = SQUARE_SIZE
        self.piece_color = {
            'player_1': str(WOOD),
            'player_2': str(WHITE)
        }

    # Method to remove pieces from the board
    def remove(self, args):
        color = args['piece']
        if color != str(0):
            if color == str(WOOD):
                self.red_left -= 1  # Update the count of remaining red pieces
            else:
                self.white_left -= 1  # Update the count of remaining white pieces

        left_pieces = {
            'red_left': self.red_left,
            'white_left': self.white_left,
        }

        return left_pieces

    # Method to get valid moves for a given piece
    def get_config_moves(self, args):
        # Get valid moves for a given piece
        piece = args['piece']
        row = piece['row']
        col = piece['col']
        color = piece['color']

        left = col
        _left = left - 1
        right = col
        _right = right + 1

        config = {
            'wood': {
                # args = (row - 1, max(row - 3, -1), -1, piece.color, _left)
                'left_bottom_to_top': {
                    'start': row - 1,
                    'stop': max(row - 3, -1),
                    'step': -1,
                    'color': color,
                    'left': _left
                },
                # args = (row - 1, max(row - 3, -1), -1, piece.color, _right)
                'right_bottom_to_top': {
                    'start': row - 1,
                    'stop': max(row - 3, -1),
                    'step': -1,
                    'color': color,
                    'right': _right
                }
            },
            'white': {
                # args = (row + 1, min(row + 3, ROWS), 1, piece.color, _left)
                'left_top_to_bottom': {
                    'start': row + 1,
                    'stop': min(row + 3, ROWS),
                    'step': 1,
                    'color': color,
                    'left': _left
                },
                # args = (row + 1, min(row + 3, ROWS), 1, piece.color, _right)
                'right_top_to_bottom': {
                    'start': row + 1,
                    'stop': min(row + 3, ROWS),
                    'step': 1,
                    'color': color,
                    'right': _right
                }
            },
            'king': {
                # args = (row - 1, 0, -1, piece.color, _left)
                'left_bottom_to_top': {
                    'start': row - 1,
                    'stop': max(row - 3, -1),
                    'step': -1,
                    'color': color,
                    'left': _left
                },
                # args = (row - 1, 0, -1, piece.color, _right)
                'right_bottom_to_top': {
                    'start': row - 1,
                    'stop': max(row - 3, -1),
                    'step': -1,
                    'color': color,
                    'right': _right
                },
                # args = (row + 1, ROWS, 1, piece.color, _left)
                'left_top_to_bottom': {
                    'start': row + 1,
                    'stop': min(row + 3, ROWS),
                    'step': 1,
                    'color': color,
                    'left': _left
                },
                # args = (row + 1, ROWS, 1, piece.color, _right)
                'right_top_to_bottom': {
                    'start': row + 1,
                    'stop': min(row + 3, ROWS),
                    'step': 1,
                    'color': color,
                    'right': _right
                }
            },
        }
        return config
