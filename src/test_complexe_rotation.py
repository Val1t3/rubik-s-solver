#!/usr/bin/env python3

import copy
from termcolor import colored

from cube import Cube

def main() -> None:
    """
    Test the rotation of the cube - FBRLUD format.
    """

    # Initialize a solved cube.
    cube = Cube.Cube()
    cube.faces[Cube.Cube.FRONT] = ["W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9"]
    cube.faces[Cube.Cube.RIGHT] = ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9"]
    cube.faces[Cube.Cube.LEFT] = ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"]
    cube.faces[Cube.Cube.UP] = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9"]
    cube.faces[Cube.Cube.DOWN] = ["O1", "O2", "O3", "O4", "O5", "O6", "O7", "O8", "O9"]
    cube.faces[Cube.Cube.BACK] = ["Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9"]

    cube_f = copy.deepcopy(cube)
    cube_f.rotate("F")
    cube_f.display_cube()
    if cube_f.faces[Cube.Cube.FRONT] == ["W7", "W4", "W1", "W8", "W5", "W2", "W9", "W6", "W3"]\
        and cube_f.faces[Cube.Cube.RIGHT] == ["R7", "G2", "G3", "R8", "G5", "G6", "R9", "G8", "G9"]\
        and cube_f.faces[Cube.Cube.LEFT] == ["B1", "B2", "O1", "B4", "B5", "O2", "B7", "B8", "O3"]\
        and cube_f.faces[Cube.Cube.UP] == ["R1", "R2", "R3", "R4", "R5", "R6", "B9", "B6", "B3"]\
        and cube_f.faces[Cube.Cube.DOWN] == ["G7", "G4", "G1", "O4", "O5", "O6", "O7", "O8", "O9"]\
        and cube_f.faces[Cube.Cube.BACK] == ["Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9"]:
        print(colored("F move is correct.", "green"))
    else:
        print(colored("F move is incorrect.", "red"))


if __name__ == "__main__":
    main()