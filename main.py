import random

player = 'O'
ai = 'X'
depth = 9

board = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]
exampleBoard = [['1', '2', '3'],
                ['4', '5', '6'],
                ['7', '8', '9']]


def printBoard(customBoard):
    for row in range(3):
        print(customBoard[row])


def movesLeft():
    for row in range(3):
        for col in range(3):
            if board[row][col] == '_':
                return True
    return False


def isGameOver():
    for row in range(3):
        if(board[row][0] == board[row][1] and board[row][0] == board[row][2]):
            if(board[row][0] == player):
                return True
            elif(board[row][0] == ai):
                return True
    for col in range(3):
        if(board[0][col] == board[1][col] and board[0][col] == board[2][col]):
            if(board[0][col] == player):
                return True
            elif(board[0][col] == ai):
                return True
    if (board[0][0] == board[1][1] and board[0][0] == board[2][2]):
        if (board[0][0] == player):
            return True
        elif (board[0][0] == ai):
            return True
    if (board[2][0] == board[1][1] and board[2][0] == board[0][2]):
        if (board[2][0] == player):
            return True
        elif (board[2][0] == ai):
            return True
    if movesLeft():
        return False
    else:
        return True


def isWinScore():
    for row in range(3):
        if(board[row][0] == board[row][1] and board[row][0] == board[row][2]):
            if(board[row][0] == player):
                return -1
            elif(board[row][0] == ai):
                return 1
    for col in range(3):
        if(board[0][col] == board[1][col] and board[0][col] == board[2][col]):
            if(board[0][col] == player):
                return -1
            elif(board[0][col] == ai):
                return 1
    if (board[0][0] == board[1][1] and board[0][0] == board[2][2]):
        if (board[0][0] == player):
            return -1
        elif (board[0][0] == ai):
            return 1
    if (board[2][0] == board[1][1] and board[2][0] == board[0][2]):
        if (board[2][0] == player):
            return -1
        elif (board[2][0] == ai):
            return 1
    return 0


def minMax(boardState, depth, alpha, beta, maxMove):
    if depth == 0 or isGameOver():
        return [-1, -1, isWinScore()]
    if maxMove:
        bestMove = [-1, -1, -100]
        for row in range(3):
            for col in range(3):
                if boardState[row][col] == '_':
                    boardState[row][col] = ai
                    score = minMax(boardState, depth - 1, alpha, beta, False)
                    boardState[row][col] = '_'
                    score[0] = row
                    score[1] = col
                    if score[2] > bestMove[2]:
                        bestMove = score
                    alpha = max(alpha, score[2])
                    if beta <= alpha:
                        break
            if beta <= alpha:
                break
        return bestMove
    else:
        bestMove = [-1, -1, 100]
        for row in range(3):
            for col in range(3):
                if boardState[row][col] == '_':
                    boardState[row][col] = player
                    score = minMax(boardState, depth - 1, alpha, beta, True)
                    boardState[row][col] = '_'
                    score[0] = row
                    score[1] = col
                    if score[2] < bestMove[2]:
                        bestMove = score
                    beta = min(beta, score[2])
                    if beta <= alpha:
                        break
            if beta <= alpha:
                break
        return bestMove


def humanMove():
    printBoard(exampleBoard)
    print("Please enter a number from 1 to 9 to select a free location.")
    printBoard(board)
    humanInput = int(input())
    valid = False
    while not valid:
        if humanInput == 1 and board[0][0] == '_':
            board[0][0] = 'O'
            valid = True
        elif humanInput == 2 and board[0][1] == '_':
            board[0][1] = 'O'
            valid = True
        elif humanInput == 3 and board[0][2] == '_':
            board[0][2] = 'O'
            valid = True
        elif humanInput == 4 and board[1][0] == '_':
            board[1][0] = 'O'
            valid = True
        elif humanInput == 5 and board[1][1] == '_':
            board[1][1] = 'O'
            valid = True
        elif humanInput == 6 and board[1][2] == '_':
            board[1][2] = 'O'
            valid = True
        elif humanInput == 7 and board[2][0] == '_':
            board[2][0] = 'O'
            valid = True
        elif humanInput == 8 and board[2][1] == '_':
            board[2][1] = 'O'
            valid = True
        elif humanInput == 9 and board[2][2] == '_':
            board[2][2] = 'O'
            valid = True
        else:
            print("Invalid Move.")
            print("Please enter a number from 1 to 9 to select a free location.")
            humanInput = int(input())
            valid = False


while not isGameOver():
    if depth % 2 == 1:
        if depth == 9:
            board[random.randint(0, 2)][random.randint(0, 2)] = ai
        else:
            move = minMax(board, depth, -100, 100, True)
            board[move[0]][move[1]] = ai
    else:
        humanMove()
    depth -= 1

if isWinScore() == -1:
    print("Congrats! You Win! This Is VERY RARE!")
elif isWinScore() == 0:
    print("Tie Game! Better Luck Next Time!")
else:
    print("AI Wins! Better Luck Next Time! You're Going To Need It!")
printBoard(board)
