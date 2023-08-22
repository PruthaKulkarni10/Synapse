import random

class ChessPlayer:
  def members(self,name,age,elo,rating,tenacity,isBoring):
    self.name=name
    self.age=age
    self.elo=elo
    self.rating=rating
    self.tenacity=tenacity
    self.isBoring=isBoring

    tournament_score=0
    
def simulateMatch(player1,player2):
  elo_diff=player1.elo-player2.elo

  if elo_diff>100:
    winner=player1 if player1>player2 else player2

  if player1.isBoring or player2.isBoring:
    if elo_diff<100:
      winner=None

  if winner==player1:
    player1.tournament_score+=1

  elif winner==player2:
    player2.tournament_score+=1

  else:
    player1.tournament_score+=0.5
    player2.tournament_score=+0.5

  
  
players=[
    ChessPlayer("Courage the Cowardly Dog", 25, 1000.39, 1000, False),
    ChessPlayer("Princess Peach", 23, 945.65, 50, True),
    ChessPlayer("Walter White", 50, 1650.73, 750, False),
    ChessPlayer("Rory Gilmore", 16, 1700.87, 500, False),
    ChessPlayer("Anthony Fantano", 37, 1400.45, 400, True),
    ChessPlayer("Beth Harmon", 20, 2500.34, 150, False)
 ]
 
for i in range(len(players)):
    for j in range(i + 1, len(players)):
        simulateMatch(players[i], players[j])
        simulateMatch(players[j], players[i])

# Sort players based on tournament score
players.sort(key=lambda player: player.tournament_score, reverse=True)

# Print the final table of results
print("Final Table of Results:")
print("{:<30} {:<10} {:<10}".format("Name", "Age", "Tournament Score"))
print("-" * 50)

for player in players:
    print("{:<30} {:<10} {:<10}".format(player.name, player.age, player.tournament_score))