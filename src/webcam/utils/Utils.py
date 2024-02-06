#!/usr/bin/env python3

from termcolor import colored

class Utils:

    """
    Class to manage utils functions.
    """

    def __init__(self):
        pass


    def display_face(self, face: list) -> None:
        print(f"{face[0:3]}\n{face[3:6]}\n{face[6:9]}\n")


    def display_color(self, color: str) -> str:
        if color[0] == "W":
            return colored(color, "white")
        elif color[0] == "G":
            return colored(color, "green")
        elif color[0] == "B":
            return colored(color, "blue")
        elif color[0] == "R":
            return colored(color, "red")
        elif color[0] == "O":
            return colored(color, "magenta")
        elif color[0] == "Y":
            return colored(color, "yellow")
        else:
            return color