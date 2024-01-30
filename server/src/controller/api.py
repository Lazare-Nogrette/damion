# controller/api.py
from flask import jsonify, request
from src.config import app
from src.model.game import Game

game = Game()

@app.route('/game/init', methods=['GET'])
def init_game():
    # Access the "value" parameter from the query string
    try:
        #value = request.args.get('config')
        # print('Init Game: ', value)
        print('----------Init Game--------------')

        game = Game()
        # config = game.config
        config = {
            'white_left': game.Board.white_left,
            'red_left': game.Board.red_left,
            'nbr_rows': game.Board.rows,
            'nbr_cols': game.Board.cols,
            'windows_size': game.Board.window_size,
            'piece_color': game.Board.piece_color
        }
        print('The Game config is: ', config)
        print('-----------------------')
        return jsonify({'config': config})
    except Exception as e:
        print('Error: ', str(e))
        print('-----------------------')
        # return jsonify({'result': 'error', 'message': str(e)})
        return jsonify({'error': str(e)})


@app.route('/game/change_turn', methods=['GET'])
def get_turn():
    # Access the "value" parameter from the query string
    try:
        value = request.args.get('turn')
        print('Value of turn: ', value)
        print('-----------------------')
        turn = game.change_turn(value)
        return jsonify({'turn': turn})
    except Exception as e:
        print('Error: ', str(e))
        print('-----------------------')
        # return jsonify({'result': 'error', 'message': str(e)})
        return jsonify({'error': str(e)})

@app.route('/board/config_moves', methods=['POST'])
def get_config_moves():
    try:
        data = request.get_json()

        print('Value moves: ', data)
        print('-----------------------')
        moves = game.Board.get_config_moves(data)
        return jsonify({'config': moves})
    except Exception as e:
        print('Error: ', str(e))
        print('-----------------------')
        # return jsonify({'result': 'error', 'message': str(e)})
        return jsonify({'error': str(e)})

@app.route('/piece/remove', methods=['POST'])
def remove_piece():
    # Access the "value" parameter from the query string
    try:
        data = request.get_json()
        print('Value to remove: ', data)
        print('-----------------------')
        left_pieces = game.Board.remove(data)
        return jsonify({'left_pieces': left_pieces})
    except Exception as e:
        print('Error: ', str(e))
        print('-----------------------')
        # return jsonify({'result': 'error', 'message': str(e)})
        return jsonify({'error': str(e)})

@app.route('/piece/calc_position', methods=['POST'])
def calculate_position():
    try:
        data = request.get_json()

        print('Value Piece position: ', data)
        print('-----------------------')
        position = game.Board.Piece.calc_pos(data)
        return jsonify({'position': position})
    except Exception as e:
        print('Error: ', str(e))
        print('-----------------------')
        # return jsonify({'result': 'error', 'message': str(e)})
        return jsonify({'error': str(e)})
