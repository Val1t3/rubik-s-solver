#!/usr/bin/env python3

import sys

from webcam.Webcam import Webcam
from cube.Cube import Cube
from algorithm.Solver import Solver

def main() -> None:
    for arg in sys.argv[1:]:
        if arg == "-h" or arg == "--help":
            help()
        else:
            cube = Cube()
            Webcam(cube).run()
    sys.exit(0)


def help() -> None:
    print("Usage: python3 main.py [options]\n")
    print("OPTIONS:")
    print("  -h, --help\t\tDisplay this help message.")
    print()
    print("USAGE:")
    print("    1: Scan FRONT face.")
    print("    2: Scan RIGHT face.")
    print("    3: Scan LEFT face.")
    print("    4: Scan UP face.")
    print("    5: Scan DOWN face.")
    print("    6: Scan BACK face.")
    print()
    print("    a: Solve the Rubik's Cube.")
    print("    q: Quit the program.")
    sys.exit(0)


if __name__ == "__main__":
    main()