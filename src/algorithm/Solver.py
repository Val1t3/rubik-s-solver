#!/usr/bin/env python3

from src.cube.Cube import Cube

class Solver:

    """
    Class to resolve the Rubik's Cube.
    """

    POSITION = [
        "Line 1",
        "Line 2",
        "Line 3",
        "Column 1",
        "Column 2",
        "Column 3"
    ]

    MOVEMENT = [
        "Right",
        "Left",
        "Up",
        "Down"
    ]

    def __init__(self, cube: Cube) -> None:
        self.cube = cube
        self.moves = []

    def solve(self) -> None:
        print("Solving...")
        print(f"{self.POSITION[0]} - {self.MOVEMENT[0]}")

    def get_moves(self) -> list:
        return self.moves