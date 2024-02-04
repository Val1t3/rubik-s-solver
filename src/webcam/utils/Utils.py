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


    def display_color(self, color: chr) -> chr:
        if color == "W":
            return colored(color, "white")
        elif color == "G":
            return colored(color, "green")
        elif color == "B":
            return colored(color, "blue")
        elif color == "R":
            return colored(color, "red")
        elif color == "O":
            return colored(color, "magenta")
        elif color == "Y":
            return colored(color, "yellow")
        else:
            return color