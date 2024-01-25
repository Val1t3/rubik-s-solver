#!/usr/bin/env python3

from src.webcam.utils.Utils import Utils

class Cube:

    """
    Class to manage the Rubik's Cube.
    """

    FRONT = 0
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4
    BACK = 5


    def __init__(self):
        self.faces = {
            self.FRONT: ["X", "X", "X", "X", "X", "X", "X", "X", "X"],
            self.BACK: ["X", "X", "X", "X", "X", "X", "X", "X", "X"],
            self.LEFT: ["X", "X", "X", "X", "X", "X", "X", "X", "X"],
            self.RIGHT: ["X", "X", "X", "X", "X", "X", "X", "X", "X"],
            self.UP: ["X", "X", "X", "X", "X", "X", "X", "X", "X"],
            self.DOWN: ["X", "X", "X", "X", "X", "X", "X", "X", "X"]
        }


    def set_face(self, face: int, colors: list) -> None:
        self.faces[face] = colors

        if face == self.FRONT:
            self.faces[self.FRONT][4] = "W"
        elif face == self.BACK:
            self.faces[self.BACK][4] = "Y"
        elif face == self.LEFT:
            self.faces[self.LEFT][4] = "G"
        elif face == self.RIGHT:
            self.faces[self.RIGHT][4] = "B"
        elif face == self.UP:
            self.faces[self.UP][4] = "O"
        elif face == self.DOWN:
            self.faces[self.DOWN][4] = "R"


    def get_face(self, face: str) -> list:
        return self.faces[face]


    def display_cube(self) -> None:
        print(f"... {self.faces[self.UP][0]}{self.faces[self.UP][1]}{self.faces[self.UP][2]} ... ...")
        print(f"... {self.faces[self.UP][3]}{self.faces[self.UP][4]}{self.faces[self.UP][5]} ... ...")
        print(f"... {self.faces[self.UP][6]}{self.faces[self.UP][7]}{self.faces[self.UP][8]} ... ...")
        print()
        print(f"{self.faces[self.LEFT][0]}{self.faces[self.LEFT][1]}{self.faces[self.LEFT][2]} {self.faces[self.FRONT][0]}{self.faces[self.FRONT][1]}{self.faces[self.FRONT][2]} {self.faces[self.RIGHT][0]}{self.faces[self.RIGHT][1]}{self.faces[self.RIGHT][2]} {self.faces[self.BACK][0]}{self.faces[self.BACK][1]}{self.faces[self.BACK][2]}")
        print(f"{self.faces[self.LEFT][3]}{self.faces[self.LEFT][4]}{self.faces[self.LEFT][5]} {self.faces[self.FRONT][3]}{self.faces[self.FRONT][4]}{self.faces[self.FRONT][5]} {self.faces[self.RIGHT][3]}{self.faces[self.RIGHT][4]}{self.faces[self.RIGHT][5]} {self.faces[self.BACK][3]}{self.faces[self.BACK][4]}{self.faces[self.BACK][5]}")
        print(f"{self.faces[self.LEFT][6]}{self.faces[self.LEFT][7]}{self.faces[self.LEFT][8]} {self.faces[self.FRONT][6]}{self.faces[self.FRONT][7]}{self.faces[self.FRONT][8]} {self.faces[self.RIGHT][6]}{self.faces[self.RIGHT][7]}{self.faces[self.RIGHT][8]} {self.faces[self.BACK][6]}{self.faces[self.BACK][7]}{self.faces[self.BACK][8]}")
        print()
        print(f"... {self.faces[self.DOWN][0]}{self.faces[self.DOWN][1]}{self.faces[self.DOWN][2]} ... ...")
        print(f"... {self.faces[self.DOWN][3]}{self.faces[self.DOWN][4]}{self.faces[self.DOWN][5]} ... ...")
        print(f"... {self.faces[self.DOWN][6]}{self.faces[self.DOWN][7]}{self.faces[self.DOWN][8]} ... ...")