"""Find the solutions to the n queens problem from all permutations."""

import collections
import itertools
import unittest

def is_solution(board):
    """Return whether board contains a solution to the n queens problem.

    Args:
        board: Iterable containing the integer column where the queen can
            be found in that row.
    Returns:
        True if board contains a solution to the n queens problem.
        False otherwise.
    """
    length = len(board)
    counter = collections.Counter(board)

    # Check each column has ONLY ONE queen
    if len(counter) != length:
        return False
    column_set = frozenset(range(length))
    total = 0
    for column, count in counter.items():
        if column not in column_set:
            return False
        if count != 1:
            return False
        total += count

    # Check each row has a queen
    if total != length:
        return False

    # Check if there is a queen in rows above that can attack along diagonals
    for row, column in enumerate(board):
        for i in range(1, row + 1):
            if ((board[row-i] == (column - i)) or
                (board[row-i] == (column + i))):
                return False

    return True

def print_board(board):
    """Print the chessboard in the iterable board.

    Args:
        board: Iterable containing the integer column where the queen can
            be found in that row.
    """
    length = len(board)
    assert(max(board) < length)

    border = ('+-' * length) + '+'
    print(border)
    for column in board:
        for i in range(column):
            print('| ', end='')
        print('|Q', end='')
        for i in range(column + 1, length):
            print('| ', end='')
        print('|')
        print(border)


class _UnitTest(unittest.TestCase):
    def test_is_solution(self):
        """Test whether a board contains a solution to the n queens problem."""
        self.assertTrue(is_solution([0]))
        self.assertFalse(is_solution([0, 1]))
        self.assertFalse(is_solution([0, 1, 2]))
        self.assertFalse(is_solution([0, 1, 2, 3]))
        self.assertTrue(is_solution([1, 3, 0, 2]))
        self.assertTrue(is_solution([2, 0, 3, 1]))
        self.assertFalse(is_solution((0, 1)))
        self.assertFalse(is_solution((0, 1, 2)))
        self.assertFalse(is_solution((0, 1, 2, 3)))
        self.assertTrue(is_solution((1, 3, 0, 2)))
        self.assertTrue(is_solution((2, 0, 3, 1)))

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '-n', type=int, default=8,
        help='positive integer number of queens')
    args = parser.parse_args()

    if (args.n <= 0) or (args.n in (2, 3)):
        # There are no solutions for 2 or 3 queens
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(_UnitTest)
        unittest.TextTestRunner(verbosity=2).run(suite)
        parser.exit()

    count = 0
    for board in itertools.permutations(range(args.n)):
        if is_solution(board):
            count += 1
            print_board(board)
            print()
    print('{} solutions'.format(count))
