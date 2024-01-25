#!/usr/bin/env python3

import cv2

class ColorParser:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height


    def parse(self, frame) -> str:
        # GET AVERAGE COLOR
        average_color = self.get_average_color(frame)
        # GET COLOR NAME
        color_name = self.get_color_name(average_color)
        # RETURN COLOR NAME
        print(f"color name -> {color_name}")
        return color_name


    def get_color_on_pos(self, frame, pos: int, size: int) -> tuple:
        average_color = cv2.mean(frame[pos[1]:pos[1]+size, pos[0]:pos[0]+size])
        return average_color


    def get_average_color(self, frame) -> tuple:
        size = 30
        pos  = (int(self.width / 2 - size * 1.8), int(self.height / 2 - size * 1.8))
        print(f"get color position -> {pos}")

        average_color = cv2.mean(frame[pos[1]:pos[1]+size, pos[0]:pos[0]+size])
        print(average_color)

        # Calculate the center of the detection area
        center_of_detection = (pos[0] + size // 2, pos[1] + size // 2)
        print(f"center of detection -> {center_of_detection}")

        # DEBUG
        cv2.circle(frame, center_of_detection, 5, (0, 255, 0), -1)  # Green dot
        cv2.rectangle(frame, pos, (pos[0] + size, pos[1] + size), (255, 0, 0), 2)  # Blue rectangle

        return average_color


    def get_color_name(self, average_color: tuple) -> str:
        # BGR
        print(average_color)
        res = (int(average_color[0]), int(average_color[1]), int(average_color[2]))
        print(res)
        if res[0] >= 100 and res[1] >= 100 and res[2] >= 100:
            return "W"
        elif res[0] > res[1] and res[0] > res[2]:
            return "B"
        elif res[1] > res[0] and res[1] > res[2]:
            return "G"
        elif res[2] > res[0] and res[2] > res[1]:
            if res[1] < 150 and res[0] < 10:
                return "O"
            elif res[1] > 150 and res[0] < 10:
                return "Y"
            else:
                return "R"
        return "X"
