import unittest
from src.hanoi import Hanoi
from src.solver import Solver

class TestHanoi(unittest.TestCase):

    def test_move_disk(self):
        hanoi = Hanoi(3)
        hanoi.move_disk(1, 'A', 'B')
        self.assertEqual(hanoi.get_moves(), [(1, 'A', 'B')])

    def test_solve(self):
        hanoi = Hanoi(3)
        moves = hanoi.solve()
        self.assertEqual(len(moves), 7)  # 2^3 - 1 moves for 3 disks

    def test_solver(self):
        solver = Solver()
        moves = solver.solve_hanoi(3)
        self.assertEqual(len(moves), 7)  # 2^3 - 1 moves for 3 disks

if __name__ == '__main__':
    unittest.main()