# Import needed libraries and helper files
import titlecard
import coin

# Show ascii title card
titlecard.displayTitlecard()

# Assign player names, use a class for players
class Player:
    winCounter = 0
    name = ""

Player1, Player2 = Player(), Player()

Player1.name = input("Enter Player 1's Name: ")
Player2.name = input("Enter Player 2's Name: ")

# Coin Toss for who goes first
callIt = input(Player1.name, " please call either Heads or Tails")
# verify input here, search a list of acceptable inputs?

# flip the coin
coinface = coin.toss()

# Assign X or O to first player, other player gets the unselected choice

# Draw the board

# Prompt for square 
# Loop until a player wins or cat game occurs
    # Start checking for a win at turn 5 
    # Stop checking after turn 9 as no other possible moves

# Display who winner or draw if noone won

# Prompt to play again with current game scorecard

# If no is chosen, display final scorecard and congratule winner
 
