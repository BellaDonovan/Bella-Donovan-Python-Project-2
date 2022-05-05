from tkinter import *
import random

def nextTurn(row, column):
    global player
    xWins = 0
    oWins = 0

    if buttons[row][column]['text'] == '' and checkWinner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player
            if checkWinner() is False:
                player = players[1]
                label.config(text=(players[1]+ '\'s Turn'))

            elif checkWinner() is True:
                label.config(text=(players[0] + ' wins!'))
                if player[0] == 'X':
                    xWins += 1
                    xWinsLabel.config(text=f'X : {xWins} wins')
                else:
                    oWins += 1
                    oWinsLabel.config(text=f'O : {oWins} wins')

            elif checkWinner() == 'Tie':
                label.config(text=('It\'s a Tie!'))
        else:
            buttons[row][column]['text'] = player
            if checkWinner() is False:
                player = players[0]
                label.config(text=(players[0] + '\'s Turn'))
            elif checkWinner():
                label.config(text=(players[1] + ' wins!'))
                if players[1] == 'X':
                    xWins += 1
                    xWinsLabel.config(text=f'X : {xWins} wins')
                else:
                    oWins += 1
                    oWinsLabel.config(text=f'O : {oWins} wins')

            elif checkWinner() == 'Tie':
                label.config(text=('It\'s a Tie!'))


def checkWinner():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != '':
            buttons[row][0].config(bg='green')
            buttons[row][1].config(bg='green')
            buttons[row][2].config(bg='green')
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != '':
            buttons[0][column].config(bg='green')
            buttons[1][column].config(bg='green')
            buttons[2][column].config(bg='green')
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        buttons[0][0].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][2].config(bg='green')
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        buttons[0][2].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][0].config(bg='green')
        return True

    elif not emptySpaces():
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg='blue')
        return 'Tie'

    else:
        return False


def emptySpaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != '':
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True

def newGame():
    global player
    player = random.choice(players)
    label.config(text=player + '\'s Turn')

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text='', bg='#F0F0F0')

def resetScore():
    oWinsLabel.config(text=f'O : 0 wins')
    xWinsLabel.config(text=f'X : 0 wins')

window = Tk()
window.title('Tic Tac Toe')
players = ['X', 'O']
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
label = Label(text= player + '\'s Turn')
label.pack(side ='top')

resetButton = Button(text='Start New Game', command=newGame)
resetButton.pack(side='top')

scoreLabel = Label(text='Current Score')
xWinsLabel = Label(text='X : 0 wins')
oWinsLabel = Label(text='O : 0 wins')
oWinsLabel.pack(side='bottom')
xWinsLabel.pack(side='bottom')
scoreLabel.pack(side='bottom')
resetScoreButton = Button(text='Reset Score', command=resetScore)
resetScoreButton.pack(side='bottom')

frame = Frame(window)
frame.pack()


for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text='', width=5, height=2, command=lambda row=row, column=column: nextTurn(row, column))
        buttons[row][column].grid(row=row,column=column)

window.mainloop()