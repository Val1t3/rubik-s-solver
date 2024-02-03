#!/usr/bin/env python3

from src.webcam.Webcam import Webcam
from src.cube.Cube import Cube
from src.algorithm.Solver import Solver

def main() -> None:
    cube = Cube()
    Webcam(cube).run()


if __name__ == "__main__":
    main()