import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.games = dict['games']
        self.id = dict['id']
    
    def __str__(self):
        return f"{self.name:20}\t{self.team}\t{self.goals:2} + {self.assists:2} = {self.goals + self.assists}"

class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.json = requests.get(url).json()
        self.players = []
        for player_dict in self.json:
            player = Player(player_dict)
            self.players.append(player)

class PlayerStats:
    def __init__(self, reader):
        self.players = reader.players
    
    def top_scorers_by_nationality(self, nationality: str):
        response = []

        for player in self.players:
            if player.nationality == nationality:
                response.append(player)
        
        response.sort(key=lambda player: player.goals + player.assists, reverse=True)
        return response
