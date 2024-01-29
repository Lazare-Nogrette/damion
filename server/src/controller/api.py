# controller/api.py
from flask import jsonify, request
from config import app
from model.game import Game

game = Game()

@app.route('/game/init', methods=['GET'])
def init_game():
    # Access the "value" parameter from the query string
        return jsonify({})


@app.route('/game/change_turn', methods=['GET'])
def get_turn():
    # Access the "value" parameter from the query string
    return jsonify({})

@app.route('/board/config_moves', methods=['POST'])
def get_config_moves():
    return jsonify({})

@app.route('/piece/remove', methods=['POST'])
def remove_piece():
    return jsonify({})

@app.route('/piece/calc_position', methods=['POST'])
def calculate_position():
    return jsonify({})
