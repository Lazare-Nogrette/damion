# Fichier: serveur.py
from src.config import app
from src.controller import api
from src.config.conf import PORT


if __name__ == '__main__':
    app.run(port=PORT)
