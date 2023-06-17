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
    x_count = 0
    o_count = 0
    for row in board:
        for place in row:
            if place == X:
                x_count += 1
            elif place == O:
                o_count += 1
    if x_count > o_count:
        return O
    else:
        return X
        
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    for i, row in enumerate(board):
        for j, place in enumerate(row):
            if place == EMPTY:
                actions_set.add((i, j))
    return actions_set

    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    pl = player(board)
    i, j = action
    if new_board[i][j] != EMPTY:
        raise Exception
    else:
        new_board[i][j] = pl
    return new_board

    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    set_c = set()
    set_d = set()
    for i in range(3):
        set_a = set()
        set_b = set()
        for j in range(3):
            set_a.add(board[i][j])
            set_b.add(board[j][i])
            if i == j:
                set_c.add(board[i][j])
            if (i + j) == 2:
                set_d.add(board[i][j])
        # print(set_a)
        # print(set_b)
            
        if len(set_a) == 1:
            ele = list(set_a)[0]
            if ele != EMPTY:
                return ele
        if len(set_b) == 1:
            elem = list(set_b)[0]
            if elem != EMPTY:
                return elem
    # print(set_c)
    # print(set_d)
    if len(set_c) == 1:
        elems = list(set_c)[0]
        if elems != EMPTY:
            return elems
    if len(set_d) == 1:
        elemts = list(set_d)[0]
        if elemts != EMPTY:
            return elemts
    return None  
    
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    else:
        for row in board:
            if EMPTY in row:
                return False 
        return True
        
        
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        win = winner(board)
        if win == X:
            return 1
        elif win == O:
            return -1
        else:
            return 0
    # raise NotImplementedError
def max_value(board):
    if terminal(board):
        return utility(board)
    else:
        v = -float('inf')
        actions_set = actions(board)
        for action in actions_set:
            v = max(v, min_value(result(board, action)))
        return v 

def min_value(board):
    if terminal(board):
        return utility(board)
    else:
        v = float('inf')
        actions_set = actions(board)
        for action in actions_set:
            v = min(v, max_value(result(board, action)))
        return v



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    pl = player(board)
    action_set = actions(board)
    if pl == X:
        possible_actions = {}
        v = -float('inf')
        for action in action_set:
            min_val = min_value(result(board, action))
            possible_actions[min_val] = action
            if min_val >= v:
                v = min_val
        return possible_actions[v]
    elif pl == O:
        possible_actions = {}
        v = float('inf')
        for action in action_set:
            max_val = max_value(result(board, action))
            possible_actions[max_val] = action
            if max_val <= v:
                v = max_val
        return possible_actions[v]
            


    raise NotImplementedError
