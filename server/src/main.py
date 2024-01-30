# Fichier: serveur.py
from config import app
from controller import api
from config.conf import PORT


if __name__ == '__main__':
    app.run(port=PORT)
