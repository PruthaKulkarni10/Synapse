import random

class ChessPlayer:
    def __init__(self, name, age, elo, tenacity, isBoring):
        self.name = name
        self.age = age
        self.elo = elo
        self.tenacity = tenacity
        self.isBoring = isBoring

        self.tournament_score = 0  # Initialize tournament score

def simulateMatch(player1, player2):
    elo_diff = player1.elo - player2.elo
    winner = None  # Initialize winner as None

    if elo_diff > 100:
        winner = player1 if player1.elo > player2.elo else player2
    elif player1.isBoring or player2.isBoring:
        if elo_diff <= 100:
            return None, None  # Match ends in a draw if one player is boring
    else:
        random_factor = random.randint(1, 10)
        lower_elo_player_factor = random_factor * player1.tenacity if player1.elo < player2.elo else player2.tenacity
        if lower_elo_player_factor > max(player1.elo, player2.elo):
            winner = player1 if player1.elo < player2.elo else player2

    if winner == player1:
        return player1, player2
    elif winner == player2:
        return player2, player1
    else:
        return None, None  # Match ends in a draw

players = [
    ChessPlayer("Courage the Cowardly Dog", 25, 1000.39, 1000, False),
    ChessPlayer("Princess Peach", 23, 945.65, 50, True),
    ChessPlayer("Walter White", 50, 1650.73, 750, False),
    ChessPlayer("Rory Gilmore", 16, 1700.87, 500, False),
    ChessPlayer("Anthony Fantano", 37, 1400.45, 400, True),
    ChessPlayer("Beth Harmon", 20, 2500.34, 150, False)
]

# Simulate matches
for i in range(len(players)):
    for j in range(i + 1, len(players)):
        result1, result2 = simulateMatch(players[i], players[j])
        if result1 is not None:
            result1.tournament_score += 1
        if result2 is not None:
            result2.tournament_score += 1

# Sort players based on tournament score
players.sort(key=lambda player: player.tournament_score, reverse=True)

# Print the final table of results
print("Final Table of Results:")
print("{:<30} {:<10} {:<10}".format("Name", "Age", "Tournament Score"))
print("-" * 50)

for player in players:
    print("{:<30} {:<10} {:<10}".format(player.name, player.age, player.tournament_score))
