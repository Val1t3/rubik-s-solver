#!/usr/bin/env python3

import cv2

from src.webcam.utils.Square import Square
from src.cube.Cube import Cube

class Webcam:

    def __init__(self, cube: Cube):
        self.cap = cv2.VideoCapture(0)
        self.cube = cube


    def run(self) -> None:
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            Square(frame).draw()
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('a'):
                self.check_color()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # RELEASE CAPTURE
        self.cap.release()
        cv2.destroyAllWindows()


    def draw_squares(self, frame) -> None:
        top_left_corner = (100, 100)
        square_size = 25
        color = (255, 0, 0)
        thickness = 3

        bottom_right_corner = (top_left_corner[0] + square_size, top_left_corner[1] + square_size)
        cv2.rectangle(frame, top_left_corner, bottom_right_corner, color, thickness)



    def check_color(self) -> None:
        print("color")