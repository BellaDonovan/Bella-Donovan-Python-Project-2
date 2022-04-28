from Player import HumanPlayer, RandomComputerPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for i in range(9)] #list to represent board
        self.currentWinner = None # keep track of winner

    def printBoard(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]: #represents which row
            print('| ' + ' |'.join(row) + ' |')

    @staticmethod #doesn't relate to specific board, so don't need to pass in self
    def printBoardNumbers():
        # 0 | 1 | 2 etc (tells what number corresponds to what box
        numberBoard = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in numberBoard:
            print('| ' + ' |'.join(row) + ' |')

    def availableMoves(self):
        # return []
        moves = []
        for (i, spot) in enumerate(self.board):
            # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
            if spot == ' ':
                moves.append(i)
        return moves

    def emptySquares(self):
        # returns a bool corresponding to if there is empty spaces or not
        return ' ' in self.board

    def numberEmptySquares(self):
        # returns number of empty spots in the board
        return self.board.count(' ')

    def makeMove(self, square, letter):
        # if valid, make the move and assign letter to square, return true
        # if invalid return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.currentWinner = letter
            return True
        return False

    def winner(self, square, letter):
        #winner of 3 in a row anywhere
        # checking row
        rowInd = square // 3
        row = self.board[rowInd*3 : (rowInd +1)*3]
        if all([spot == letter for spot in row]):
            return True

        #checking column
        colInd = square % 3
        column = [self.board[colInd + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        # if all fail
        return False

def play(game, xPlayer, oPlayer, printGame=True):
    # returns winner of the game (letter) or None for a tie
    if printGame:
        game.printBoardNumbers()

    letter = 'x' #starting letter
    # iterate while game has empty squares
    while game.emptySquares():
        # get move from the right player
        if letter == 'o':
            square = oPlayer.getMove(game)
        else:
            square = xPlayer.getMove(game)

        if game.makeMove(square, letter):
            if printGame:
                print(letter + f'makes a move to square {square}')
                game.printBoard()
                print('') # empty line

            if game.currentWinner:
                if printGame:
                    print(letter, 'wins!!')
                return letter

            #need to alternate player
            if letter == 'x':
                letter = 'o'
            else:
                letter = 'x'

        #pause to make the game easier to read
        time.sleep(0.8)

    if printGame:
        print('It is a tie!')

if __name__ == '__main__':
    xPlayer = HumanPlayer('x')
    oPlayer = RandomComputerPlayer('o')
    t = TicTacToe()
    play(t, xPlayer, oPlayer, printGame = True)