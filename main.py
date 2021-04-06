# arr = [['9', '1', '10'], ['0', '9', '10', '11', '2'], ['1', '10', '11', '12', '3'], ['2', '11', '12', '13', '4'], ['3', '12', '13', '14', '5'], ['4', '13', '14', '15', '6'], ['5', '14', '15', '16', '7'], ['6', '15', '16', '17', '8'], ['7', '16', '17'], ['0', '1', '10', '19', '18'], ['0', '1', '2', '9', '11', '18', '19', '20'], ['1', '2', '3', '10', '12', '19', '20', '21'], ['2', '3', '4', '11', '13', '20', '21', '22'], ['3', '4', '5', '12', '14', '21', '22', '23'], ['4', '5', '6', '13', '15', '22', '23', '24'], ['5', '6', '7', '14', '16', '23', '24', '25'], ['6', '7', '8', '15', '17', '24', '25', '26'], ['7', '8', '16', '25', '26'], ['9', '10', '19', '28', '27'], ['9', '10', '11', '18', '20', '27', '28', '29'], ['10', '11', '12', '19', '21', '28', '29', '30'], ['11', '12', '13', '20', '22', '29', '30', '31'], ['12', '13', '14', '21', '23', '30', '31', '32'], ['13', '14', '15', '22', '14', '31', '32', '33'], ['14', '15', '16', '23', '25', '32', '33', '34'], ['15', '16', '17', '24', '26', '33', '34', '35'], ['16', '17', '25', '34', '35']]

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

	while cell > 0:
		neighbour_column.append(cell)
		cell = cell -9
		
		
	cell = myCell

	while cell < 80:
		neighbour_column.append(cell)
		cell = cell + 9

	neighbour_column = list(dict.fromkeys(neighbour_column))
		
	neighbour_column.sort()



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



	return neighbour_row



def getSquareNeighbours(board, cell):
	squareDict = {1: [0,1,2,9,10,11,18,19,20], 2: [3,4,5,12,13,14,21,22,23], 3: [6,7,8,15,16,17,24,25,26], 4: [27,28,29,36,37,38,45,46,47], 5: [30,31,31,39,40,41,48,49,50], 6: [33,34,35,42,43,44,51,52,53], 7: [54,55,56,63,64,65,72,73,74], 8: [57,58,59,66,67,68,75,76,77], 9: [60,61,62,69,70,71,78,79,80]}

	


# board =  generateBoard()

# print(generateRowNeighbours(board, board[8][5]))
# print(getColumnNeighbours(board, board[8][8]))



