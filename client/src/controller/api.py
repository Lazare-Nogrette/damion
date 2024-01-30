import requests
from config.conf import HOST_API
from config.constants import WOOD, WHITE

class GameAPI():
    def __init__(self):
        pass

    def change_turn(self, turn):
        try:
            response = requests.get(HOST_API + '/game/change_turn?turn=' + str(turn))
            response = response.json()
            # print('response: ', response)
            get_turn = response['turn']
            player = 'Wood Piece'
            if get_turn == str(WOOD):
                print('---------- Player 1 -------------')
                player = 'Wood Piece'
            else:
                print('---------- Player 2 -------------')
                player = 'White Piece'
            print('User turn: ', player)
            print('-----------------------')
            return get_turn
        except Exception as e:
            print('Error: ', str(e))
            print('-----------------------')
            return False

    def get_config(self, args):
        try:
            response = requests.post(HOST_API + '/board/config_moves', json=args)
            response = response.json()
            # print('response: ', response)
            get_config_moves = response['config']
            print('---------- FREE MOVEMENTS -------------')
            print('=========>')
            print(f'Get config moves: ${get_config_moves}')
            print('<=========')
            print('-----------------------')
            return get_config_moves
        except Exception as e:
            print('Error: ', str(e))
            print('-----------------------')
            return {}

    def remove_piece(self, args):
        try:
            # print(f'Valid Piece to remove: {args}')
            response = requests.post(HOST_API + '/piece/remove', json=args)
            response = response.json()
            # print('response: ', response)
            get_removed_pieces = response['left_pieces']
            print('++++++++++ LEFT PIECES +++++++++++++')
            print('Removed Pieces left are: ', get_removed_pieces)
            print('+++++++++++++++++++++++')
            return get_removed_pieces
        except Exception as e:
            print('Error: ', str(e))
            print('-----------------------')
            return None

    def calculate_position(self, args):
        try:
            response = requests.post(HOST_API + '/piece/calc_position', json=args)
            response = response.json()
            # print('response: ', response)
            get_piece_position = response['position']
            print('----------POSITION------------')
            print('Piece position is: ', get_piece_position)
            print('-----------------------')
            return get_piece_position
        except Exception as e:
            print('Error: ', str(e))
            print('-----------------------')
            return None
        
    def init_game(self):
        print('----------Initializing Board------------')
        try:
            response = requests.get(HOST_API + '/game/init')
            response = response.json()
            # print('response: ', response)
            get_game_config = response['config']

            print('>>>>>>>>>>Connected to the server: ',HOST_API)
            print('The Game config is: ', get_game_config)
            print('-----------------------')
            return get_game_config
        except Exception as e:
            print('>>>>>>>>>>Cannot connect to the server: ', HOST_API)
            print('Error: ', str(e))
            print('-----------------------')
            return None
