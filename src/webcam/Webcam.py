#!/usr/bin/env python3

import cv2

from src.webcam.utils.Square import Square
from src.cube.Cube import Cube
from src.webcam.parser.ColorParser import ColorParser
from src.algorithm.Solver import Solver

class Webcam:

    """
    Main class to manage the webcam and Rubik's Cube colors detection.
    """

    def __init__(self, cube: Cube):
        self.cap = cv2.VideoCapture(0)
        self.cube = cube
        self.frame_name = "Rubik's Resolver"
        self.width, self.height = 200, 200


    def run(self) -> None:
        while True:
            ret, frame = self.cap.read()

            # ERROR HANDLING
            if not ret:
                print("Can't receive frame. Exiting ...")
                break

            if self.width == 200 and self.height == 200:
                try:
                    _, _, self.width, self.height = cv2.getWindowImageRect(self.frame_name)
                except:
                    self.width, self.height = 200, 200

            Square(frame).draw(self.width, self.height)
            cv2.imshow(self.frame_name, frame)
            self.input_management(cv2.waitKey(1), frame)


    def input_management(self, key: int, frame) -> None:
        if key == ord('q'):
            self.cap.release()
            cv2.destroyAllWindows()
        elif key == ord('a'):
            Solver(self.cube).solve()
        elif key == ord('&'):
            self.cube.set_face(Cube.FRONT, self.check_color(frame))
            self.cube.display_cube()
        elif key == ord('é'):
            self.cube.set_face(Cube.RIGHT, self.check_color(frame))
            self.cube.display_cube()
        elif key == ord('"'):
            self.cube.set_face(Cube.LEFT, self.check_color(frame))
            self.cube.display_cube()
        elif key == ord("'"):
            self.cube.set_face(Cube.UP, self.check_color(frame))
            self.cube.display_cube()
        elif key == ord('('):
            self.cube.set_face(Cube.DOWN, self.check_color(frame))
            self.cube.display_cube()
        elif key == ord('§'):
            self.cube.set_face(Cube.BACK, self.check_color(frame))
            self.cube.display_cube()


    def check_color(self, frame) -> list:
        return ColorParser(self.width, self.height).parse(frame)