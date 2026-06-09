class Hanoi:
    def __init__(self, num_disks):
        self.num_disks = num_disks
        self.moves = []

    def move_disk(self, from_peg, to_peg):
        self.moves.append((from_peg, to_peg))

    def solve(self, n, from_peg, to_peg, aux_peg):
        if n == 1:
            self.move_disk(from_peg, to_peg)
            return
        self.solve(n - 1, from_peg, aux_peg, to_peg)
        self.move_disk(from_peg, to_peg)
        self.solve(n - 1, aux_peg, to_peg, from_peg)

    def get_moves(self):
        return self.moves