#!/usr/bin/env python3

from webcam.Webcam import Webcam
from cube.Cube import Cube
from algorithm.Solver import Solver

def main() -> None:
    cube = Cube()
    Webcam(cube).run()


if __name__ == "__main__":
    main()