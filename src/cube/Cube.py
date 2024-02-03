#!/usr/bin/env python3

import copy

from webcam.utils.Utils import Utils

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
            self.faces[self.LEFT][4] = "B"
        elif face == self.RIGHT:
            self.faces[self.RIGHT][4] = "G"
        elif face == self.UP:
            self.faces[self.UP][4] = "R"
        elif face == self.DOWN:
            self.faces[self.DOWN][4] = "O"


    def get_face(self, face: str) -> list:
        return self.faces[face]


    def display_cube(self) -> None:
        print(f"\n... {self.faces[self.UP][0]}{self.faces[self.UP][1]}{self.faces[self.UP][2]} ... ...")
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


    def rotate(self, movement: str) -> None:
        save = copy.deepcopy(self.faces)

        if movement == "U":
            self.faces[self.UP][0] = save[self.UP][6]
            self.faces[self.UP][1] = save[self.UP][3]
            self.faces[self.UP][2] = save[self.UP][0]
            self.faces[self.UP][3] = save[self.UP][7]
            self.faces[self.UP][5] = save[self.UP][1]
            self.faces[self.UP][6] = save[self.UP][8]
            self.faces[self.UP][7] = save[self.UP][5]
            self.faces[self.UP][8] = save[self.UP][2]
            self.faces[self.LEFT][0] = save[self.FRONT][0]
            self.faces[self.LEFT][1] = save[self.FRONT][1]
            self.faces[self.LEFT][2] = save[self.FRONT][2]
            self.faces[self.FRONT][0] = save[self.RIGHT][0]
            self.faces[self.FRONT][1] = save[self.RIGHT][1]
            self.faces[self.FRONT][2] = save[self.RIGHT][2]
            self.faces[self.RIGHT][0] = save[self.BACK][0]
            self.faces[self.RIGHT][1] = save[self.BACK][1]
            self.faces[self.RIGHT][2] = save[self.BACK][2]
            self.faces[self.BACK][0] = save[self.LEFT][0]
            self.faces[self.BACK][1] = save[self.LEFT][1]
            self.faces[self.BACK][2] = save[self.LEFT][2]
        elif movement == "U'":
            self.faces[self.UP][0] = save[self.UP][2]
            self.faces[self.UP][1] = save[self.UP][5]
            self.faces[self.UP][2] = save[self.UP][8]
            self.faces[self.UP][3] = save[self.UP][1]
            self.faces[self.UP][5] = save[self.UP][7]
            self.faces[self.UP][6] = save[self.UP][0]
            self.faces[self.UP][7] = save[self.UP][3]
            self.faces[self.UP][8] = save[self.UP][6]
            self.faces[self.LEFT][0] = save[self.BACK][0]
            self.faces[self.LEFT][1] = save[self.BACK][1]
            self.faces[self.LEFT][2] = save[self.BACK][2]
            self.faces[self.BACK][0] = save[self.RIGHT][0]
            self.faces[self.BACK][1] = save[self.RIGHT][1]
            self.faces[self.BACK][2] = save[self.RIGHT][2]
            self.faces[self.RIGHT][0] = save[self.FRONT][0]
            self.faces[self.RIGHT][1] = save[self.FRONT][1]
            self.faces[self.RIGHT][2] = save[self.FRONT][2]
            self.faces[self.FRONT][0] = save[self.LEFT][0]
            self.faces[self.FRONT][1] = save[self.LEFT][1]
            self.faces[self.FRONT][2] = save[self.LEFT][2]
        elif movement == "D":
            self.faces[self.DOWN][0] = save[self.DOWN][6]
            self.faces[self.DOWN][1] = save[self.DOWN][3]
            self.faces[self.DOWN][2] = save[self.DOWN][0]
            self.faces[self.DOWN][3] = save[self.DOWN][7]
            self.faces[self.DOWN][5] = save[self.DOWN][1]
            self.faces[self.DOWN][6] = save[self.DOWN][8]
            self.faces[self.DOWN][7] = save[self.DOWN][5]
            self.faces[self.DOWN][8] = save[self.DOWN][2]
            self.faces[self.LEFT][6] = save[self.FRONT][6]
            self.faces[self.LEFT][7] = save[self.FRONT][7]
            self.faces[self.LEFT][8] = save[self.FRONT][8]
            self.faces[self.FRONT][6] = save[self.RIGHT][6]
            self.faces[self.FRONT][7] = save[self.RIGHT][7]
            self.faces[self.FRONT][8] = save[self.RIGHT][8]
            self.faces[self.RIGHT][6] = save[self.BACK][6]
            self.faces[self.RIGHT][7] = save[self.BACK][7]
            self.faces[self.RIGHT][8] = save[self.BACK][8]
            self.faces[self.BACK][6] = save[self.LEFT][6]
            self.faces[self.BACK][7] = save[self.LEFT][7]
            self.faces[self.BACK][8] = save[self.LEFT][8]
        elif movement == "D'":
            self.faces[self.DOWN][0] = save[self.DOWN][2]
            self.faces[self.DOWN][1] = save[self.DOWN][5]
            self.faces[self.DOWN][2] = save[self.DOWN][8]
            self.faces[self.DOWN][3] = save[self.DOWN][1]
            self.faces[self.DOWN][5] = save[self.DOWN][7]
            self.faces[self.DOWN][6] = save[self.DOWN][0]
            self.faces[self.DOWN][7] = save[self.DOWN][3]
            self.faces[self.DOWN][8] = save[self.DOWN][6]
            self.faces[self.LEFT][6] = save[self.BACK][6]
            self.faces[self.LEFT][7] = save[self.BACK][7]
            self.faces[self.LEFT][8] = save[self.BACK][8]
            self.faces[self.BACK][6] = save[self.RIGHT][6]
            self.faces[self.BACK][7] = save[self.RIGHT][7]
            self.faces[self.BACK][8] = save[self.RIGHT][8]
            self.faces[self.RIGHT][6] = save[self.FRONT][6]
            self.faces[self.RIGHT][7] = save[self.FRONT][7]
            self.faces[self.RIGHT][8] = save[self.FRONT][8]
            self.faces[self.FRONT][6] = save[self.LEFT][6]
            self.faces[self.FRONT][7] = save[self.LEFT][7]
            self.faces[self.FRONT][8] = save[self.LEFT][8]
        elif movement == "R":
            self.faces[self.RIGHT][0] = save[self.RIGHT][6]
            self.faces[self.RIGHT][1] = save[self.RIGHT][3]
            self.faces[self.RIGHT][2] = save[self.RIGHT][0]
            self.faces[self.RIGHT][3] = save[self.RIGHT][7]
            self.faces[self.RIGHT][5] = save[self.RIGHT][1]
            self.faces[self.RIGHT][6] = save[self.RIGHT][8]
            self.faces[self.RIGHT][7] = save[self.RIGHT][5]
            self.faces[self.RIGHT][8] = save[self.RIGHT][2]
            self.faces[self.UP][2] = save[self.FRONT][2]
            self.faces[self.UP][5] = save[self.FRONT][5]
            self.faces[self.UP][8] = save[self.FRONT][8]
            self.faces[self.FRONT][2] = save[self.DOWN][2]
            self.faces[self.FRONT][5] = save[self.DOWN][5]
            self.faces[self.FRONT][8] = save[self.DOWN][8]
            self.faces[self.DOWN][2] = save[self.BACK][6]
            self.faces[self.DOWN][5] = save[self.BACK][3]
            self.faces[self.DOWN][8] = save[self.BACK][0]
            self.faces[self.BACK][0] = save[self.UP][8]
            self.faces[self.BACK][3] = save[self.UP][5]
            self.faces[self.BACK][6] = save[self.UP][2]
        elif movement == "R'":
            self.faces[self.RIGHT][0] = save[self.RIGHT][2]
            self.faces[self.RIGHT][1] = save[self.RIGHT][5]
            self.faces[self.RIGHT][2] = save[self.RIGHT][8]
            self.faces[self.RIGHT][3] = save[self.RIGHT][1]
            self.faces[self.RIGHT][5] = save[self.RIGHT][7]
            self.faces[self.RIGHT][6] = save[self.RIGHT][0]
            self.faces[self.RIGHT][7] = save[self.RIGHT][3]
            self.faces[self.RIGHT][8] = save[self.RIGHT][6]
            self.faces[self.UP][2] = save[self.BACK][0]
            self.faces[self.UP][5] = save[self.BACK][3]
            self.faces[self.UP][8] = save[self.BACK][6]
            self.faces[self.BACK][0] = save[self.DOWN][8]
            self.faces[self.BACK][3] = save[self.DOWN][5]
            self.faces[self.BACK][6] = save[self.DOWN][2]
            self.faces[self.DOWN][2] = save[self.FRONT][2]
            self.faces[self.DOWN][5] = save[self.FRONT][5]
            self.faces[self.DOWN][8] = save[self.FRONT][8]
            self.faces[self.FRONT][2] = save[self.UP][2]
            self.faces[self.FRONT][5] = save[self.UP][5]
            self.faces[self.FRONT][8] = save[self.UP][8]
        elif movement == "L":
            self.faces[self.LEFT][0] = save[self.LEFT][6]
            self.faces[self.LEFT][1] = save[self.LEFT][3]
            self.faces[self.LEFT][2] = save[self.LEFT][0]
            self.faces[self.LEFT][3] = save[self.LEFT][7]
            self.faces[self.LEFT][5] = save[self.LEFT][1]
            self.faces[self.LEFT][6] = save[self.LEFT][8]
            self.faces[self.LEFT][7] = save[self.LEFT][5]
            self.faces[self.LEFT][8] = save[self.LEFT][2]
            self.faces[self.UP][0] = save[self.BACK][2]
            self.faces[self.UP][3] = save[self.BACK][5]
            self.faces[self.UP][6] = save[self.BACK][8]
            self.faces[self.BACK][2] = save[self.DOWN][6]
            self.faces[self.BACK][5] = save[self.DOWN][3]
            self.faces[self.BACK][8] = save[self.DOWN][0]
            self.faces[self.DOWN][0] = save[self.FRONT][0]
            self.faces[self.DOWN][3] = save[self.FRONT][3]
            self.faces[self.DOWN][6] = save[self.FRONT][6]
            self.faces[self.FRONT][0] = save[self.UP][0]
            self.faces[self.FRONT][3] = save[self.UP][3]
            self.faces[self.FRONT][6] = save[self.UP][6]
        elif movement == "L'":
            self.faces[self.LEFT][0] = save[self.LEFT][2]
            self.faces[self.LEFT][1] = save[self.LEFT][5]
            self.faces[self.LEFT][2] = save[self.LEFT][8]
            self.faces[self.LEFT][3] = save[self.LEFT][1]
            self.faces[self.LEFT][5] = save[self.LEFT][7]
            self.faces[self.LEFT][6] = save[self.LEFT][0]
            self.faces[self.LEFT][7] = save[self.LEFT][3]
            self.faces[self.LEFT][8] = save[self.LEFT][6]
            self.faces[self.UP][0] = save[self.FRONT][0]
            self.faces[self.UP][3] = save[self.FRONT][3]
            self.faces[self.UP][6] = save[self.FRONT][6]
            self.faces[self.FRONT][0] = save[self.DOWN][0]
            self.faces[self.FRONT][3] = save[self.DOWN][3]
            self.faces[self.FRONT][6] = save[self.DOWN][6]
            self.faces[self.DOWN][0] = save[self.BACK][8]
            self.faces[self.DOWN][3] = save[self.BACK][5]
            self.faces[self.DOWN][6] = save[self.BACK][2]
            self.faces[self.BACK][2] = save[self.UP][6]
            self.faces[self.BACK][5] = save[self.UP][3]
            self.faces[self.BACK][8] = save[self.UP][0]
        elif movement == "F":
            self.faces[self.FRONT][0] = save[self.FRONT][6]
            self.faces[self.FRONT][1] = save[self.FRONT][3]
            self.faces[self.FRONT][2] = save[self.FRONT][0]
            self.faces[self.FRONT][3] = save[self.FRONT][7]
            self.faces[self.FRONT][5] = save[self.FRONT][1]
            self.faces[self.FRONT][6] = save[self.FRONT][8]
            self.faces[self.FRONT][7] = save[self.FRONT][5]
            self.faces[self.FRONT][8] = save[self.FRONT][2]
            self.faces[self.UP][6] = save[self.LEFT][8]
            self.faces[self.UP][7] = save[self.LEFT][5]
            self.faces[self.UP][8] = save[self.LEFT][2]
            self.faces[self.LEFT][2] = save[self.DOWN][0]
            self.faces[self.LEFT][5] = save[self.DOWN][1]
            self.faces[self.LEFT][8] = save[self.DOWN][2]
            self.faces[self.DOWN][0] = save[self.RIGHT][6]
            self.faces[self.DOWN][1] = save[self.RIGHT][3]
            self.faces[self.DOWN][2] = save[self.RIGHT][0]
            self.faces[self.RIGHT][0] = save[self.UP][8]
            self.faces[self.RIGHT][3] = save[self.UP][7]
            self.faces[self.RIGHT][6] = save[self.UP][6]
        elif movement == "F'":
            self.faces[self.FRONT][0] = save[self.FRONT][2]
            self.faces[self.FRONT][1] = save[self.FRONT][5]
            self.faces[self.FRONT][2] = save[self.FRONT][8]
            self.faces[self.FRONT][3] = save[self.FRONT][1]
            self.faces[self.FRONT][5] = save[self.FRONT][7]
            self.faces[self.FRONT][6] = save[self.FRONT][0]
            self.faces[self.FRONT][7] = save[self.FRONT][3]
            self.faces[self.FRONT][8] = save[self.FRONT][6]
            self.faces[self.UP][6] = save[self.RIGHT][0]
            self.faces[self.UP][7] = save[self.RIGHT][3]
            self.faces[self.UP][8] = save[self.RIGHT][6]
            self.faces[self.LEFT][2] = save[self.UP][8]
            self.faces[self.LEFT][5] = save[self.UP][7]
            self.faces[self.LEFT][8] = save[self.UP][6]
            self.faces[self.DOWN][0] = save[self.LEFT][2]
            self.faces[self.DOWN][1] = save[self.LEFT][5]
            self.faces[self.DOWN][2] = save[self.LEFT][8]
            self.faces[self.RIGHT][0] = save[self.DOWN][2]
            self.faces[self.RIGHT][3] = save[self.DOWN][1]
            self.faces[self.RIGHT][6] = save[self.DOWN][0]
        elif movement == "B":
            self.faces[self.BACK][0] = save[self.BACK][6]
            self.faces[self.BACK][1] = save[self.BACK][3]
            self.faces[self.BACK][2] = save[self.BACK][0]
            self.faces[self.BACK][3] = save[self.BACK][7]
            self.faces[self.BACK][5] = save[self.BACK][1]
            self.faces[self.BACK][6] = save[self.BACK][8]
            self.faces[self.BACK][7] = save[self.BACK][5]
            self.faces[self.BACK][8] = save[self.BACK][2]
            self.faces[self.UP][0] = save[self.RIGHT][2]
            self.faces[self.UP][1] = save[self.RIGHT][5]
            self.faces[self.UP][2] = save[self.RIGHT][8]
            self.faces[self.RIGHT][2] = save[self.DOWN][8]
            self.faces[self.RIGHT][5] = save[self.DOWN][7]
            self.faces[self.RIGHT][8] = save[self.DOWN][6]
            self.faces[self.DOWN][6] = save[self.LEFT][0]
            self.faces[self.DOWN][7] = save[self.LEFT][3]
            self.faces[self.DOWN][8] = save[self.LEFT][6]
            self.faces[self.LEFT][0] = save[self.UP][0]
            self.faces[self.LEFT][3] = save[self.UP][1]
            self.faces[self.LEFT][6] = save[self.UP][2]
        elif movement == "B'":
            self.faces[self.BACK][0] = save[self.BACK][2]
            self.faces[self.BACK][1] = save[self.BACK][5]
            self.faces[self.BACK][2] = save[self.BACK][8]
            self.faces[self.BACK][3] = save[self.BACK][1]
            self.faces[self.BACK][5] = save[self.BACK][7]
            self.faces[self.BACK][6] = save[self.BACK][0]
            self.faces[self.BACK][7] = save[self.BACK][3]
            self.faces[self.BACK][8] = save[self.BACK][6]
            self.faces[self.UP][0] = save[self.LEFT][6]
            self.faces[self.UP][1] = save[self.LEFT][3]
            self.faces[self.UP][2] = save[self.LEFT][0]
            self.faces[self.LEFT][0] = save[self.DOWN][6]
            self.faces[self.LEFT][3] = save[self.DOWN][7]
            self.faces[self.LEFT][6] = save[self.DOWN][8]
            self.faces[self.DOWN][6] = save[self.RIGHT][8]
            self.faces[self.DOWN][7] = save[self.RIGHT][5]
            self.faces[self.DOWN][8] = save[self.RIGHT][2]
            self.faces[self.RIGHT][2] = save[self.UP][2]
            self.faces[self.RIGHT][5] = save[self.UP][1]
            self.faces[self.RIGHT][8] = save[self.UP][0]


    def format_colors(self, colors: list) -> str:
        res = "".join(colors)
        res = res.replace("W", "F")
        res = res.replace("B", "L")
        res = res.replace("Y", "B")
        res = res.replace("R", "U")
        res = res.replace("G", "R")
        res = res.replace("O", "D")

        return res


    def cube_to_list(self) -> list:
        colors_list = []
        colors_list.extend(self.get_face(Cube.UP))
        colors_list.extend(self.get_face(Cube.RIGHT))
        colors_list.extend(self.get_face(Cube.FRONT))
        colors_list.extend(self.get_face(Cube.DOWN))
        colors_list.extend(self.get_face(Cube.LEFT))
        colors_list.extend(self.get_face(Cube.BACK))

        return colors_list


    def is_solved(self) -> bool:
        return self.format_colors(self.cube_to_list()) == "FFFFFFFFFRRRRRRRRRBBBBBBBBBLLLLLLLLLDDDDDDDDD"