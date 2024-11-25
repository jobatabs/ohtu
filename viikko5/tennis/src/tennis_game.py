SCORES = ["Love", "Fifteen", "Thirty", "Forty"]

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.score = f"{SCORES[0]}-All"

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 += 1
        elif player_name == self.player2_name:
            self.m_score2 += 1

        if self.m_score1 == self.m_score2:
            self.score = f"{SCORES[self.m_score1]}-All" if self.m_score1 < 3 else "Deuce"
        elif self.m_score1 > 3 or self.m_score2 > 3:
            point_difference = self.m_score1 - self.m_score2

            if abs(point_difference) == 1:
                self.score = f"Advantage {self.player1_name}" if point_difference == 1 else f"Advantage {self.player2_name}"
            else:
                self.score = f"Win for {self.player1_name}" if point_difference >= 2 else f"Win for {self.player2_name}"
        else:
            self.score = f"{SCORES[self.m_score1]}-{SCORES[self.m_score2]}"

    def get_score(self):
        return self.score
