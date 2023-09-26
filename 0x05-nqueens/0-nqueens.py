#!/usr/bin/python3
# """ N QUEENS ALGORITHM WITH BACKTRACKING (RECURSION INSIDE LOOP) """
# import sys


# class NQueen:
#     """ Class for solving N Queen Problem """

#     def __init__(self, n):
#         """ Global Variables """
#         self.n = n
#         self.x = [0 for i in range(n + 1)]
#         self.res = []

#     def place(self, k, i):
#         """ Checks if k Queen can be placed in i column (True)
#         or if the are attacking queens in row or diagonal (False)
#         """

#         # j checks from 1 to k - 1 (Up to previous queen)
#         for j in range(1, k):
#             # There is already a queen in column
#             # or a queen in same diagonal
#             if self.x[j] == i or \
#                abs(self.x[j] - i) == abs(j - k):
#                 return 0
#         return 1

#     def nQueen(self, k):
#         """ Tries to place every queen in the board
#         Args:
#         k: starting queen from which to evaluate (should be 1)
#         """
#         # i goes from column 1 to column n (1st column is 1st index)
#         for i in range(1, self.n + 1):
#             if self.place(k, i):
#                 # Queen can be placed in i column
#                 self.x[k] = i
#                 if k == self.n:
#                     # Placed all 4 Queens (A solution was found)
#                     solution = []
#                     for i in range(1, self.n + 1):
#                         solution.append([i - 1, self.x[i] - 1])
#                     self.res.append(solution)
#                 else:
#                     # Need to place more Queens
#                     self.nQueen(k + 1)
#         return self.res


# # Main

# if len(sys.argv) != 2:
#     print("Usage: nqueens N")
#     sys.exit(1)

# N = sys.argv[1]

# try:
#     N = int(N)
# except ValueError:
#     print("N must be a number")
#     sys.exit(1)

# if N < 4:
#     print("N must be at least 4")
#     sys.exit(1)

# queen = NQueen(N)
# res = queen.nQueen(1)

# for i in res:
#     print(i)



'''N queens solution finder module.
'''
import sys


solutions = []
'''The list of possible solutions to the N queens problem.
'''
n = 0
'''The size of the chessboard.
'''
pos = None
'''The list of possible positions on the chessboard.
'''


def get_input():
    '''Retrieves and validates this program's argument.
    Returns:
        int: The size of the chessboard.
    '''
    global n
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(pos0, pos1):
    '''Checks if the positions of two queens are in an attacking mode.
    Args:
        pos0 (list or tuple): The first queen's position.
        pos1 (list or tuple): The second queen's position.
    Returns:
        bool: True if the queens are in an attacking position else False.
    '''
    if (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]):
        return True
    return abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])


def group_exists(group):
    '''Checks if a group exists in the list of solutions.
    Args:
        group (list of integers): A group of possible positions.
    Returns:
        bool: True if it exists, otherwise False.
    '''
    global solutions
    for stn in solutions:
        i = 0
        for stn_pos in stn:
            for grp_pos in group:
                if stn_pos[0] == grp_pos[0] and stn_pos[1] == grp_pos[1]:
                    i += 1
        if i == n:
            return True
    return False


def build_solution(row, group):
    '''Builds a solution for the n queens problem.
    Args:
        row (int): The current row in the chessboard.
        group (list of lists of integers): The group of valid positions.
    '''
    global solutions
    global n
    if row == n:
        tmp0 = group.copy()
        if not group_exists(tmp0):
            solutions.append(tmp0)
    else:
        for col in range(n):
            a = (row * n) + col
            matches = zip(list([pos[a]]) * len(group), group)
            used_positions = map(lambda x: is_attacking(x[0], x[1]), matches)
            group.append(pos[a].copy())
            if not any(used_positions):
                build_solution(row + 1, group)
            group.pop(len(group) - 1)


def get_solutions():
    '''Gets the solutions for the given chessboard size.
    '''
    global pos, n
    pos = list(map(lambda x: [x // n, x % n], range(n ** 2)))
    a = 0
    group = []
    build_solution(a, group)


n = get_input()
get_solutions()
for solution in solutions:
    print(solution)