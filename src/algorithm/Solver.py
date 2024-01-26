#!/usr/bin/env python3

from src.cube.Cube import Cube

class Solver:

    """
    Class to resolve the Rubik's Cube.
    """

    MOVEMENTS = [
        "U",
        "U'",
        "U2",
        "D",
        "D'",
        "D2",
        "R",
        "R'",
        "R2",
        "L",
        "L'",
        "L2",
        "F",
        "F'",
        "F2",
        "B",
        "B'",
        "B2"
    ]

    def __init__(self, cube: Cube) -> None:
        self.cube = cube
        self.moves = []

    def solve(self) -> None:
        print("Solving...")
        print(f"{self.MOVEMENTS[0]}")

    def get_moves(self) -> list:
        return self.moves