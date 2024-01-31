#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = []
    for i in range(n):
        board.append([' ' for _ in range(n)])
    return board


def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    return [list(row) for row in board]


def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    return [[r, c] for r in range(len(board)) for c in range(len(board[r])) if board[r][c] == "Q"]


def xout(board, row, col):
    """X out spots on a chessboard where non-attacking queens can no longer be played."""
    n = len(board)
    for i in range(n):
        board[row][i] = "x"
        board[i][col] = "x"
        if row+i < n and col+i < n:
            board[row+i][col+i] = "x"
        if row-i >= 0 and col-i >= 0:
            board[row-i][col-i] = "x"
        if row+i < n and col-i >= 0:
            board[row+i][col-i] = "x"
        if row-i >= 0 and col+i < n:
            board[row-i][col+i] = "x"
    board[row][col] = "Q"


def recursive_solve(board, row, solutions):
    """Recursively solve the N-queens puzzle."""
    if row == len(board):
        solutions.append(get_solution(board))
        return

    for col in range(len(board)):
        if board[row][col] == ' ':
            new_board = board_deepcopy(board)
            xout(new_board, row, col)
            recursive_solve(new_board, row + 1, solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(n)
    solutions = []
    recursive_solve(board, 0, solutions)
    for solution in solutions:
        print(solution)
