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
