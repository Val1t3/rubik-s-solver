#!/usr/bin/env python3

import cv2

from src.webcam.utils.Square import Square
from src.cube.Cube import Cube
from src.webcam.parser.ColorParser import ColorParser

class Webcam:

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
                print("Can't receive frame (stream end?). Exiting ...")
                break

            if self.width == 200 and self.height == 200:
                try:
                    _, _, self.width, self.height = cv2.getWindowImageRect(self.frame_name)
                except:
                    self.width, self.height = 200, 200

            Square(frame).draw(self.width, self.height)
            # self.check_color(frame)
            cv2.imshow(self.frame_name, frame)
            if cv2.waitKey(1) & 0xFF == ord('a'):
                self.check_color(frame)
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break

        # RELEASE CAPTURE
        self.cap.release()
        cv2.destroyAllWindows()


    def check_color(self, frame) -> None:
        ColorParser(self.width, self.height).parse(frame)