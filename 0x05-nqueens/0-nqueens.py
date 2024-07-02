#!/usr/bin/python3
""" N queens puzzle
"""

import sys


def print_usage_and_exit(message):
    print(message)
    sys.exit(1)


def is_valid(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    def backtrack(row):
        if row == N:
            print([[i, board[i]] for i in range(N)])
            return
        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(row + 1)

    board = [-1] * N
    backtrack(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N")

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")

    if N < 4:
        print_usage_and_exit("N must be at least 4")

    solve_nqueens(N)
