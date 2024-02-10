#!/usr/bin/env python3

import copy
import kociemba

from cube.Cube import Cube

class Solver:

    """
    Class to resolve the Rubik's Cube.
    """

    MOVEMENTS = [
        "U",
        "U'",
        "L",
        "L'",
        "R",
        "R'",
        "F",
        "F'",
        "B",
        "B'",
        "D",
        "D'"
    ]

    def __init__(self, cube: Cube) -> None:
        self.cube = cube
        self.moves = []


    def solve(self) -> None:
        res_list  = ""
        i = 0

        while True:
            cube_str = Cube().format_colors(self.cube.cube_to_list())
            if not self.error_handling(cube_str):
                return
            res = kociemba.solve(cube_str)
            res_list += res + " "
            for move in res.split():
                if move[-1] == "2":
                    self.cube.rotate(move[:-1])
                    self.cube.rotate(move[:-1])
                else:
                    self.cube.rotate(move)
            if self.cube.is_solved():
                break
            i += 1

        self.display_moves(res_list)


    def error_handling(self, cube_str: str) -> bool:
        # Check for correct cube string length
        if len(cube_str) != 54:
            print("Error: The cube string must be 54 characters long.")
            return False

        # Check for correct center pieces
        center_pieces_indices = [4, 13, 22, 31, 40, 49]
        expected_centers = 'URFDLB'
        for i, center in zip(center_pieces_indices, expected_centers):
            if cube_str[i] != center:
                print(f"Error: Center piece for {center} face is incorrect. Found {cube_str[i]}")
                return False

        # Check for correct count of each color
        for color in 'URFDLB':
            count = cube_str.count(color)
            if count != 9:
                print(f"Error: Color {color} count mismatch. Found {count}, expected 9.")
                return False

        # Check if cube is already solved
        if cube_str == "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB":
            print("Cube already solved.")
            return False

        return True


    def display_moves(self, moves: str) -> None:
        loop = 0
        list_moves = moves.split(" ")

        print("\n### MOVES ###")
        for i in range(0, len(list_moves), 5):
            print(loop, end="-> ")
            print(" ".join(list_moves[i:i+5]))
            print()
            loop += 1
        print("#############\n")