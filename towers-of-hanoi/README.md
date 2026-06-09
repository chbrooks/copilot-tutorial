# Towers of Hanoi

The Towers of Hanoi is a classic problem in computer science and mathematics that involves moving a set of disks from one peg to another, following specific rules. The objective is to move all the disks from the source peg to the destination peg using an auxiliary peg, while adhering to the following constraints:

1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty peg.
3. No larger disk may be placed on top of a smaller disk.

## Project Overview

This project provides an implementation of the Towers of Hanoi problem in Python. It includes classes and functions to solve the problem, visualize the moves, and test the implementation.

## Project Structure

```
towers-of-hanoi
├── src
│   ├── hanoi.py        # Implementation of the Towers of Hanoi problem
│   ├── solver.py       # Solver for the Towers of Hanoi problem
│   └── visualizer.py    # Visualization of the solution
├── tests
│   └── test_hanoi.py   # Unit tests for the implementation
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
└── main.py              # Entry point for the application
```

## Installation

To install the required dependencies, run the following command:

```
pip install -r requirements.txt
```

## Usage

To run the project, execute the `main.py` file:

```
python main.py
```

You can modify the number of disks in the `main.py` file to see how the solution changes.

## Example

For example, if you want to solve the Towers of Hanoi problem with 3 disks, the output will show the sequence of moves required to transfer the disks from the source peg to the destination peg.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.