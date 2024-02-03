#!/usr/bin/env python3

import copy
from termcolor import colored

from cube import Cube

def main() -> None:
    cube = Cube.Cube()
    cube.faces[Cube.Cube.FRONT] = ["W" for _ in cube.faces[Cube.Cube.FRONT]]
    cube.faces[Cube.Cube.RIGHT] = ["G" for _ in cube.faces[Cube.Cube.RIGHT]]
    cube.faces[Cube.Cube.LEFT] = ["B" for _ in cube.faces[Cube.Cube.LEFT]]
    cube.faces[Cube.Cube.UP] = ["R" for _ in cube.faces[Cube.Cube.UP]]
    cube.faces[Cube.Cube.DOWN] = ["O" for _ in cube.faces[Cube.Cube.DOWN]]
    cube.faces[Cube.Cube.BACK] = ["Y" for _ in cube.faces[Cube.Cube.BACK]]

    cube_u = copy.deepcopy(cube)
    cube_u.rotate("U")
    if cube_u.faces[Cube.Cube.FRONT] == ["G", "G", "G", "W", "W", "W", "W", "W", "W"]\
        and cube_u.faces[Cube.Cube.RIGHT] == ["Y", "Y", "Y", "G", "G", "G", "G", "G", "G"]\
        and cube_u.faces[Cube.Cube.LEFT] == ["W", "W", "W", "B", "B", "B", "B", "B", "B"]\
        and cube_u.faces[Cube.Cube.UP] == ["R", "R", "R", "R", "R", "R", "R", "R", "R"]\
        and cube_u.faces[Cube.Cube.DOWN] == ["O", "O", "O", "O", "O", "O", "O", "O", "O"]\
        and cube_u.faces[Cube.Cube.BACK] == ["B", "B", "B", "Y", "Y", "Y", "Y", "Y", "Y"]:
        print(colored("U move is correct.", "green"))
    else:
        print(colored("U move is incorrect.", "red"))

    cube_u_prime = copy.deepcopy(cube)
    cube_u_prime.rotate("U'")
    if cube_u_prime.faces[Cube.Cube.FRONT] == ["B", "B", "B", "W", "W", "W", "W", "W", "W"]\
        and cube_u_prime.faces[Cube.Cube.RIGHT] == ["W", "W", "W", "G", "G", "G", "G", "G", "G"]\
        and cube_u_prime.faces[Cube.Cube.LEFT] == ["Y", "Y", "Y", "B", "B", "B", "B", "B", "B"]\
        and cube_u_prime.faces[Cube.Cube.UP] == ["R", "R", "R", "R", "R", "R", "R", "R", "R"]\
        and cube_u_prime.faces[Cube.Cube.DOWN] == ["O", "O", "O", "O", "O", "O", "O", "O", "O"]\
        and cube_u_prime.faces[Cube.Cube.BACK] == ["G", "G", "G", "Y", "Y", "Y", "Y", "Y", "Y"]:
        print(colored("U' move is correct.", "green"))
    else:
        print(colored("U' move is incorrect.", "red"))

    cube_r = copy.deepcopy(cube)
    cube_r.rotate("R")
    if cube_r.faces[Cube.Cube.FRONT] == ["W", "W", "O", "W", "W", "O", "W", "W", "O"]\
        and cube_r.faces[Cube.Cube.RIGHT] == ["G", "G", "G", "G", "G", "G", "G", "G", "G"]\
        and cube_r.faces[Cube.Cube.LEFT] == ["B", "B", "B", "B", "B", "B", "B", "B", "B"]\
        and cube_r.faces[Cube.Cube.UP] == ["R", "R", "W", "R", "R", "W", "R", "R", "W"]\
        and cube_r.faces[Cube.Cube.DOWN] == ["O", "O", "Y", "O", "O", "Y", "O", "O", "Y"]\
        and cube_r.faces[Cube.Cube.BACK] == ["Y", "Y", "R", "Y", "Y", "R", "Y", "Y", "R"]:
        print(colored("R move is correct.", "green"))
    else:
        print(colored("R move is incorrect.", "red"))

    cube_r_prime = copy.deepcopy(cube)
    cube_r_prime.rotate("R'")
    if cube_r_prime.faces[Cube.Cube.FRONT] == ["W", "W", "R", "W", "W", "R", "W", "W", "R"]\
        and cube_r_prime.faces[Cube.Cube.RIGHT] == ["R", "G", "G", "R", "G", "G", "R", "G", "G"]\
        and cube_r_prime.faces[Cube.Cube.LEFT] == ["B", "B", "B", "B", "B", "B", "B", "B", "B"]\
        and cube_r_prime.faces[Cube.Cube.UP] == ["R", "R", "Y", "R", "R", "Y", "R", "R", "Y"]\
        and cube_r_prime.faces[Cube.Cube.DOWN] == ["O", "O", "W", "O", "O", "W", "O", "O", "W"]\
        and cube_r_prime.faces[Cube.Cube.BACK] == ["Y", "Y", "O", "Y", "Y", "O", "Y", "Y", "O"]:
        print(colored("R' move is correct.", "green"))
    else:
        print(colored("R' move is incorrect.", "red"))

    cube_f = copy.deepcopy(cube)
    cube_f.rotate("F")
    if cube_f.faces[Cube.Cube.FRONT] == ["W", "W", "W", "W", "W", "W", "W", "W", "W"]\
        and cube_f.faces[Cube.Cube.RIGHT] == ["R", "G", "G", "R", "G", "G", "R", "G", "G"]\
        and cube_f.faces[Cube.Cube.LEFT] == ["B", "B", "O", "B", "B", "O", "B", "B", "O"]\
        and cube_f.faces[Cube.Cube.UP] == ["R", "R", "R", "R", "R", "R", "B", "B", "B"]\
        and cube_f.faces[Cube.Cube.DOWN] == ["G", "G", "G", "O", "O", "O", "O", "O", "O"]\
        and cube_f.faces[Cube.Cube.BACK] == ["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"]:
        print(colored("F move is correct.", "green"))
    else:
        print(colored("F move is incorrect.", "red"))

    cube_f_prime = copy.deepcopy(cube)
    cube_f_prime.rotate("F'")
    if cube_f_prime.faces[Cube.Cube.FRONT] == ["W", "W", "W", "W", "W", "W", "W", "W", "W"]\
        and cube_f_prime.faces[Cube.Cube.RIGHT] == ["O", "G", "G", "O", "G", "G", "O", "G", "G"]\
        and cube_f_prime.faces[Cube.Cube.LEFT] == ["B", "B", "R", "B", "B", "R", "B", "B", "R"]\
        and cube_f_prime.faces[Cube.Cube.UP] == ["O", "O", "O", "O", "O", "O", "G", "G", "G"]\
        and cube_f_prime.faces[Cube.Cube.DOWN] == ["B", "B", "B", "O", "O", "O", "O", "O", "O"]\
        and cube_f_prime.faces[Cube.Cube.BACK] == ["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"]:
        print(colored("F' move is correct.", "green"))
    else:
        print(colored("F' move is incorrect.", "red"))


if __name__ == "__main__":
    main()