# Import needed libraries and helper files
import menu
import coin

# Show ascii title card
menu.displayTitlecard()

# Assign player names, use a class for players
class Player:
    winCounter = 0
    name = ""
    shape = ''

Player1, Player2 = Player(), Player()

Player1.name = input("Enter Player 1's Name: ")
Player2.name = input("Enter Player 2's Name: ")

# Coin Toss for who goes first
coinTossCall = input(Player1.name + ", please call either Heads or Tails: ")

correctCalls = ["Heads", "Tails", "heads", "tails"]

while coinTossCall not in correctCalls:
    coinTossCall = input("Please call either Heads or Tails: ")

# flip the coin
coinface = coin.toss()

if coinface == coinTossCall:
    print(Player1.name, " will go first!")
    startingPlayer = Player1
    secondPlayer = Player2
else:
    print(Player2.name, " will go first!")
    startingPlayer = Player2
    secondPlayer = Player1

# Assign X or O to first player, other player gets the unselected choice
shapeChoice = input(startingPlayer.name + ", choose to play as X or O: ").upper()
correctShapes = ['X', 'O']

while shapeChoice not in correctShapes:
    shapeChoice = input("Please input either X or O: ")

startingPlayer.shape = shapeChoice

if startingPlayer.shape == 'X':
    secondPlayer.shape = 'O'
else:
    secondPlayer.shape = 'X'

print(Player1.shape, Player1.name, Player1.winCounter)
print(Player2.shape, Player2.name, Player2.winCounter)
# Draw the board

# Prompt for square 
# Loop until a player wins or cat game occurs
    # Start checking for a win at turn 5 
    # Stop checking after turn 9 as no other possible moves

# Display who winner or draw if noone won

# Prompt to play again with current game scorecard

# If no is chosen, display final scorecard and congratule winner
 
