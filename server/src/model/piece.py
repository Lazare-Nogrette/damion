from config.constants import SQUARE_SIZE


class Piece:
    def __init__(self):
        pass
    # Calculate the position of the piece on the board
    def calc_pos(self, args):
        col = args['col']
        row = args['row']
        x = SQUARE_SIZE * col + SQUARE_SIZE // 2
        y = SQUARE_SIZE * row + SQUARE_SIZE // 2
        position = {
            'x': x,
            'y': y
        }
        return position
    

