#!/usr/bin/python3
"""
10. N queens (advanced)
"""

import sys


def init_board(n):
    """Initialize the `n`x`n` sized chessboard"""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)

def board_deepcopy(board):
    """Returns deepcopy of board"""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Return the list of lists within a board"""
    sol = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                sol.append([r, c])
                break
    return (sol)

def xout(board, row, col):
    """X spots on the chessboard"""
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    """X-out all rear spots"""
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    """X-out all spots below"""
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    """X-out all spots above"""
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    """X-out all spots diagonally down the right"""
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    """X-out all spots diagonally up the left"""
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    """X-out all spots diagonally up the right"""
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    """X-out all spots diagonally down the left"""
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve N-queens puzzle"""
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            temp_board = board_deepcopy(board)
            temp_board[row][c] = "Q"
            xout(temp_board, row, c)
            solutions = recursive_solve(temp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for x in solutions:
        print(x)
