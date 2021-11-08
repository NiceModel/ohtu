import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_returns_player(self):
        self.assertEqual(str(self.statistics.search("Semenko")), "Semenko EDM 4 + 12 = 16")

    def test_search_returns_empty(self):
        self.assertIsNone(self.statistics.search("John Doe"))

    def test_team_returns_players(self):
        player_names = [player.name for player in self.statistics.team("EDM")]

        self.assertEqual(player_names, ["Semenko", "Kurri", "Gretzky"])

    def test_top_scorers(self):
        top_scorers_sorted = ["Gretzky", "Lemieux", "Yzerman", "Kurri", "Semenko"]

        for i in range(5):
            top_players = [player.name for player in self.statistics.top_scorers(i)]

            self.assertEqual(top_players, top_scorers_sorted[:i+1])