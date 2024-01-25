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
            self.faces[self.LEFT][4] = "R"
        elif face == self.RIGHT:
            self.faces[self.RIGHT][4] = "O"
        elif face == self.UP:
            self.faces[self.UP][4] = "G"
        elif face == self.DOWN:
            self.faces[self.DOWN][4] = "B"


    def get_face(self, face: str) -> list:
        return self.faces[face]


    def display_cube(self) -> None:
        for face in self.faces:
            print(face)
            Utils().display_face(self.faces[face])