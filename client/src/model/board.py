import pygame
from config.constants import BLACK, ROWS, WOOD, SQUARE_SIZE, COLS, WHITE
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
        for piece in pieces:
                    # print(f'Piece Detail: {piece.__dict__}')
                    self.board[piece.row][piece.col] = 0
                    is_piece_removed = self.game_api.remove_piece({
                        'color': str(piece.color)
                    })
                    if (is_piece_removed):
                        self.red_left = is_piece_removed['red_left']
                        self.white_left = is_piece_removed['white_left']

        # print(f'Available Pieces to remove: {pieces}')

    def winner(self):
        if self.red_left <= 0:
            return WHITE
        elif self.white_left <= 0:
            return WOOD

        return None

    # Method to get valid moves for a given piece
    def get_valid_moves(self, piece):
        # Get valid moves for a given piece
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        # Check possible moves for red pieces
        if piece.color == RED:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, RED, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, RED, right))

        # Check possible moves for white pieces
        if piece.color == WHITE:
            moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, WHITE, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, WHITE, right))

        # Check possible moves for king pieces
        if piece.king:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))
            moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))

        return moves


    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        # Dictionary to store valid leftward moves as (row, col) pairs
        moves = {}
        last = []  # List to store encountered opponent pieces
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]  # Get the piece at the current position
            if current == 0:
                # If an empty square is encountered, add the possible move
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    # If there were opponent pieces, continue traversing recursively
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._traverse_left(r + step, row, step, color, left - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color:
                # If the piece is of the same color, break the loop (no more valid moves in this direction)
                break
            else:
                last = [current]  # Store the encountered opponent piece

            left -= 1

        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        # Dictionary to store valid rightward moves as (row, col) pairs
        moves = {}
        last = []  # List to store encountered opponent pieces
        for r in range(start, stop, step):
            if right >= COLS:
                break

            current = self.board[r][right]  # Get the piece at the current position
            if current == 0:
                # If an empty square is encountered, add the possible move
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    # If there were opponent pieces, continue traversing recursively
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                # If the piece is of the same color, break the loop (no more valid moves in this direction)
                break
            else:
                last = [current]  # Store the encountered opponent piece

            right += 1

        return moves

