# checks if play/number is valid at the position
def valid(bo, num, pos):
    # check row entered as [row][column]
    for i in range(len(bo[0])):
        # Check through each element in the row, and check if it is equal to the number
        # we have just inserted, we also disregard the position of the inserted number
        # as by logic, it will be true at that position.
        if bo[pos[0]][i] == num and pos[1] != i:
            return False


# Given a board, find an empty square on board at position[i][j] and return position of the square
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None
