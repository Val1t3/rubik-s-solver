#!/usr/bin/env python3

import pytwisty

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
        # TODO: Implement checking number colours verification.
        colors_list = []
        colors_list.extend(self.cube.faces[Cube.UP])
        colors_list.extend(self.cube.get_face(Cube.RIGHT))
        colors_list.extend(self.cube.get_face(Cube.FRONT))
        colors_list.extend(self.cube.get_face(Cube.DOWN))
        colors_list.extend(self.cube.get_face(Cube.LEFT))
        colors_list.extend(self.cube.get_face(Cube.BACK))

        print(Cube.UP)
        print(self.cube.faces[Cube.UP])
        print(colors_list)

        colors = self.convert_colors(colors_list)
        print(self.error_handling(colors))
        print(colors)
        result = colors
        i = 0
        while result != 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB':
            result = kociemba.solve(colors)
            print(f"{i} -> {result}")
            i += 1
        # test_result = kociemba.solve('DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD')
        # print(test_result)

    def convert_colors(self, colors: list) -> str:
        res = "".join(colors)
        res = res.replace("W", "F")
        res = res.replace("B", "L")
        res = res.replace("Y", "B")
        res = res.replace("R", "U")
        res = res.replace("G", "R")
        res = res.replace("O", "D")

        return res

    def error_handling(self, cube_str: str) -> bool:
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

        return True
