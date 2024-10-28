import unittest
from statistics_service import StatisticsService
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

class TestStatisticsService(unittest.TestCase):

    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_pelaajat_luotu(self):
        self.assertEqual(str(self.stats._players[0]), "Semenko EDM 4 + 12 = 16")
    
    def test_search(self):
        reply = self.stats.search("Semenko")
        
        self.assertEqual(str(reply), "Semenko EDM 4 + 12 = 16")
    
    def test_notfound(self):
        reply = self.stats.search("liibalaaba")

        self.assertIsNone(reply)

    def test_filter_team(self):
        reply = self.stats.team("EDM")

        self.assertEqual(str(reply[0]), "Semenko EDM 4 + 12 = 16")
    
    def test_top_dog(self):
        reply = self.stats.top(0)
        self.assertEqual(str(reply[0]), "Gretzky EDM 35 + 89 = 124")