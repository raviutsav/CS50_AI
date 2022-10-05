"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    
    cntX = 0
    cntO = 0
    
    for i in range(3):
    	for j in range(3):
    		if board[i][j] == X:
    			cntX += 1
    		if board[i][j] == O:
    			cntO += 1
    if cntX > cntO:
    	return O
    else:
    	return X
    		
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    moves = []
    for i in range(3):
    	for j in range(3):
    		if board[i][j] == None:
    			moves.append([i, j])
    return moves
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # print(action)
    if board[action[0]][action[1]] != None:
    	raise ValueError('Invalid Move')
    
    player_to_make_move = player(board)
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player_to_make_move
    return new_board
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] != None and board[0][0] == board[0][1] and board[0][1] == board[0][2]:
    	return board[0][0]
    if board[1][0] != None and board[1][0] == board[1][1] and board[1][1] == board[1][2]:
    	return board[1][0]
    if board[2][0] != None and board[2][0] == board[2][1] and board[2][1] == board[2][2]:
    	return board[2][0]
    if board[0][0] != None and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
    	return board[0][0]
    if board[0][2] != None and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
    	return board[1][1]
    if board[0][0] != None and board[0][0] == board[1][0] and board[1][0] == board[2][0]:
    	return board[0][0]
    if board[0][1] != None and board[0][1] == board[1][1] and board[1][1] == board[2][1]:
    	return board[0][1]
    if board[0][2] != None and board[0][2] == board[1][2] and board[1][2] == board[2][2]:
    	return board[0][2]
    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    # case when either of the player has won
    if winner(board) != None:
    	return True
    
    # if some spaces are left to fill then the game has not ended and tie has not happened
    cnt = 0
    for i in range(3):
    	for j in range(3):
    		if board[i][j] == None:
    			cnt += 1
    if cnt > 0:
    	return False
    else:
    	return True
    
    
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    the_winner = winner(board)
    if the_winner == X:
    	return 1
    elif the_winner == O:
    	return -1
    else:
    	return 0
    
    raise NotImplementedError

def value_of_state(board):
	
	
	ret = []
	player_should_move = [-1, -1]
	
	if terminal(board):
		ret.append(utility(board))
		ret.append(None)
		return ret
	
	player_to_make_move = player(board)
	
	if player_to_make_move == X:
		v = -math.inf
		moves = actions(board)
		for i in range(len(moves)):
			temp = value_of_state(result(board, moves[i]))[0]
			if temp > v:
				v = temp
				player_should_move = moves[i]
		ret.append(v)
		ret.append(player_should_move)
		return ret
	else:
		v = math.inf
		moves = actions(board)
		for i in range(len(moves)):
			temp = value_of_state(result(board, moves[i]))[0]
			if temp < v:
				v = temp
				player_should_move = moves[i]
		ret.append(v)
		ret.append(player_should_move)
		return ret
				
		

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
    	return None
    return value_of_state(board)[1]
    	
    	
    raise NotImplementedError
