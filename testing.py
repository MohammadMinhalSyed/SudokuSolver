from problem import problem
import math

from sudoku import solve

def generateBoard():
    board = []

    i = 0
    j = 0
    row = []

    while i < 9:

        row.append(j)

        j = j+1

        if len(row) == 9:
            board.append(row)
            row = []
            i = i+1
    return board


def getColumnNeighbours(board, myCell):

    cell = myCell
    neighbour_column = []

    while cell >= 0:
        neighbour_column.append(cell)
        cell = cell - 9

    cell = myCell

    while cell <= 80:
        neighbour_column.append(cell)
        cell = cell + 9

    neighbour_column = list(dict.fromkeys(neighbour_column))

    neighbour_column.sort()

    # neighbour_column.remove(myCell)

    return neighbour_column

# print(board)


def generateRowNeighbours(board, myCell):

    cell = myCell
    neighbour_row = []
    lowerBound = cell - cell % 9
    upperBound = lowerBound + 8

    while cell >= lowerBound:
        neighbour_row.append(cell)
        cell = cell - 1

    cell = myCell

    while cell <= upperBound:
        neighbour_row.append(cell)
        cell = cell + 1

    neighbour_row = list(dict.fromkeys(neighbour_row))

    neighbour_row.sort()

    # neighbour_row.remove(myCell)

    return neighbour_row


def getSquareNeighbours(board, cell):
    squareDict = {1: [0, 1, 2, 9, 10, 11, 18, 19, 20], 2: [3, 4, 5, 12, 13, 14, 21, 22, 23], 3: [6, 7, 8, 15, 16, 17, 24, 25, 26], 4: [27, 28, 29, 36, 37, 38, 45, 46, 47], 5: [
        30, 31, 32, 39, 40, 41, 48, 49, 50], 6: [33, 34, 35, 42, 43, 44, 51, 52, 53], 7: [54, 55, 56, 63, 64, 65, 72, 73, 74], 8: [57, 58, 59, 66, 67, 68, 75, 76, 77], 9: [60, 61, 62, 69, 70, 71, 78, 79, 80]}

    for key in squareDict:
        if cell in squareDict[key]:
            arr = squareDict[key]
            # arr.remove(cell)
    return arr


# print(getSquareNeighbours(board, cell))
# print(generateRowNeighbours(board, cell))
# print(getColumnNeighbours(board, cell))

# for a in problem:
# 	print(a)
def getNeighbours(board, cell):

    square = getSquareNeighbours(board, cell)
    row = generateRowNeighbours(board, cell)
    column = getColumnNeighbours(board, cell)

    finalNeighbourList = square + row + column

    finalNeighbourList = list(dict.fromkeys(finalNeighbourList))

    return finalNeighbourList


# Generate domain for each cell
def generateDomain():
    i = 0
    domain = {}
    while i < 81:
        domain[i] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        i = i + 1
    return domain


def updateDomain(puzzle, domain, board):

    k = 0
    newDomain = {}
    board = board

    for i in range(0, 9):
        for j in range(0, 9):
            if puzzle[i][j] == 0:

                oldDomain = domain[k]

                cell = board[i][j]

                neighbours = getNeighbours(board, cell)

                newDomain[k] = neighbours

            k = k + 1
    return newDomain


board = generateBoard()
puzzle = problem
solve(puzzle)


def test(board, puzzle):
    final = []
    for i in range(0, 9):
        rowSum = 0
        columnSum = 0
        squareSum = 0

        for j in range(0, 9):
            row = generateRowNeighbours(board, board[i][j])
            column = getColumnNeighbours(board, board[i][j])
            square = getSquareNeighbours(board, board[i][j])
            # print(row, column, square)

            y_row = math.floor(row[j]/9)
            x_row = math.floor(row[j]%9)
            rowSum += puzzle[y_row][x_row]


            x_column = math.floor(column[i]/9)
            y_column = math.floor(column[i]%9)
            columnSum += puzzle[y_column][x_column]
            # print(y_column, x_column)

            x_square = math.floor(square[j]/9)
            y_square = math.floor((square[j]%9)%3)
            # print(y_square, x_square)
            squareSum +=puzzle[y_square][x_square]
            # print(square)

        final.append(rowSum)
        final.append(columnSum)
        final.append(squareSum)
    # print(final)
    value = all(x == 45 for x in final)

    return value

print(test(board, puzzle))
# print(puzzle)


    # print(rowSum, columnSum)


        # print(row)
        # rowSum = 0
        # for a in row:
        #     y = math.floor(a/9)
        #     x = a%9
        #     print(puzzle[y][x])
        #     rowSum += puzzle[y][x]

        # columnSum = 0
        # for a in column:
        #     y = math.floor(a/9)
        #     x = a%9
        #     columnSum += puzzle[y][x]

        # squareSum = 0
        # for a in square:
        #     y = math.floor(a/9)
        #     x = a%9
        #     sum += puzzle[y][x]

        # print(rowSum)
