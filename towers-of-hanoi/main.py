from src.hanoi import Hanoi
from src.solver import Solver

def main():
    num_disks = 3  # You can change this value to test with different numbers of disks
    hanoi = Hanoi(num_disks)
    solver = Solver(hanoi)
    
    moves = solver.solve_hanoi()
    
    print("Moves to solve Towers of Hanoi:")
    for move in moves:
        print(move)

if __name__ == "__main__":
    main()