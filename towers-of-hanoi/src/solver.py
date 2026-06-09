class Solver:
    def __init__(self, hanoi):
        self.hanoi = hanoi
        self.moves = []

    def solve_hanoi(self, n, source, target, auxiliary):
        if n == 1:
            self.hanoi.move_disk(source, target)
            self.moves.append((source, target))
        else:
            self.solve_hanoi(n - 1, source, auxiliary, target)
            self.hanoi.move_disk(source, target)
            self.moves.append((source, target))
            self.solve_hanoi(n - 1, auxiliary, target, source)

    def get_moves(self):
        return self.moves