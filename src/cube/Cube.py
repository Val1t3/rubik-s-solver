#!/usr/bin/env python3

from src.webcam.utils.Utils import Utils

class Cube:

    """
    Class to manage the Rubik's Cube.
    """

    FRONT = 0
    BACK = 1
    LEFT = 2
    RIGHT = 3
    UP = 4
    DOWN = 5


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


    def get_face(self, face: str) -> list:
        return self.faces[face]


    def display_cube(self) -> None:
        for face in self.faces:
            print(face)
            Utils().display_face(self.faces[face])