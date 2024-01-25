#!/usr/bin/env python3

import cv2

class Square:

    """
    Class to manage squares to display on the webcam.
    """

    def __init__(self, frame):
        self.frame = frame
        self.size = 40
        self.color = (255, 0, 0)
        self.thickness = 3


    def draw(self, width: int, height: int) -> None:
        default_top_left_corner = (width / 2 - self.size * 1.5, height / 2 - self.size * 1.5)

        for y in range(3):
            for x in range(3):
                top_left_corner = (int(default_top_left_corner[0] + (150 * x)), int(default_top_left_corner[1] + (150 * y)))
                bottom_right_corner = (int(top_left_corner[0] + self.size), int(top_left_corner[1] + self.size))
                cv2.rectangle(self.frame, top_left_corner, bottom_right_corner, self.color, self.thickness)
