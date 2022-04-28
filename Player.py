import math
import random

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    def getMove(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def getMove(self, game):
        # Gets a random valid spot
        square = random.choice(game.availableMoves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def getMove(self, game):
        validSquare = False
        val = None
        while not validSquare:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            # Checks to make sure valid number is entered
            try:
                val = int(square)
                if val not in game.availableMoves():
                    raise ValueError
                validSquare = True
            except ValueError:
                print('Invalid Square')
        return val



