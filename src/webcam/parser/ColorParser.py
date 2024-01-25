#!/usr/bin/env python3

import cv2

from src.webcam.utils.Utils import Utils

class ColorParser:

    """
    Class to parse the colors on the webcam.
    """

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.size = 30


    def parse(self, frame) -> list:
        res = self.get_colors_on_face(frame)
        Utils().display_face(res)

        return res


    def get_colors_on_face(self, frame) -> list:
        default_pos = (int(self.width / 2 - self.size * 1.8), int(self.height / 2 - self.size * 1.8))
        colors_list = []

        for y in range(3):
            for x in range(3):
                pos = (default_pos[0] + (150 * x), default_pos[1] + (150 * y))
                colors_list.append(self.get_color_name(self.get_color_on_pos(frame, pos)))

        return colors_list


    def get_color_on_pos(self, frame, pos: int) -> tuple:
        average_color = cv2.mean(frame[pos[1]:pos[1] + self.size, pos[0]:pos[0] + self.size])
        res = (int(average_color[0]), int(average_color[1]), int(average_color[2]))

        return res


    def get_color_name(self, average_color: tuple) -> str:
        # Tuple is in BGR order.
        if average_color[0] >= 100 and average_color[1] >= 100 and average_color[2] >= 100:
            return "W"
        elif average_color[0] > average_color[1] and average_color[0] > average_color[2]:
            return "B"
        elif average_color[1] > average_color[0] and average_color[1] > average_color[2]:
            return "G"
        elif average_color[2] > average_color[0] and average_color[2] > average_color[1]:
            if average_color[1] < 150 and average_color[0] < 10:
                return "O"
            elif average_color[1] > 150 and average_color[0] < 10:
                return "Y"
            else:
                return "R"
        return "X"
