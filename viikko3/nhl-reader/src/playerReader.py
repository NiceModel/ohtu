from player import Player
import requests

class PlayerReader:
    def __init__(self, url):
        self.players = [Player(player) for player in requests.get(url).json()]

    def get_players(self):
        return self.players