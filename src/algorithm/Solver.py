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
        print("\n### Solving... ###")

        colors_list = self.colors_cube_to_list()
        if not self.error_handling(colors_list):
            return

        self.cube.set_mov("U")
        self.cube.display_cube()


    def error_handling(self, cube_str: str) -> bool:
        if len(cube_str) != 54:
            print("Error: The cube string must be 54 characters long.")
            return False

        # Check for correct center pieces
        center_pieces_indices = [4, 13, 22, 31, 40, 49]
        expected_centers = 'RGWOBY'
        for i, center in zip(center_pieces_indices, expected_centers):
            if cube_str[i] != center:
                print(f"Error: Center piece for {center} face is incorrect. Found {cube_str[i]}")
                return False

        # Check for correct count of each color
        for color in 'RGWOBY':
            count = cube_str.count(color)
            if count != 9:
                print(f"Error: Color {color} count mismatch. Found {count}, expected 9.")
                return False

        return True


    def colors_cube_to_list(self) -> list:
        colors_list = []
        colors_list.extend(self.cube.faces[Cube.UP])
        colors_list.extend(self.cube.get_face(Cube.RIGHT))
        colors_list.extend(self.cube.get_face(Cube.FRONT))
        colors_list.extend(self.cube.get_face(Cube.DOWN))
        colors_list.extend(self.cube.get_face(Cube.LEFT))
        colors_list.extend(self.cube.get_face(Cube.BACK))

        return colors_list


    def first_face_solver(self) -> list:

        return []