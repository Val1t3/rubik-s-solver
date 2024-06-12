#!/usr/bin/env python3

import cv2

class DisplayText:
    """
    Class to manage text to display on the webcam.
    """

    def __init__(self, frame):
        self.frame = frame
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.font_scale = 1
        self.font_color = (0, 200, 0)
        self.line_type = 2

        self.quit_text = "Press 'q' to quit."
        self.solution_text = "Press 'a' to solve."
        self.front_text = "Press '1' to scan FRONT face."
        self.right_text = "Press '2' to scan RIGHT face."
        self.left_text = "Press '3' to scan LEFT face."
        self.up_text = "Press '4' to scan UP face."
        self.down_text = "Press '5' to scan DOWN face."
        self.back_text = "Press '6' to scan BACK face."


    def draw(self) -> None:
        cv2.putText(self.frame, self.quit_text, (10, 30), self.font, self.font_scale, self.font_color, self.line_type)
        cv2.putText(self.frame, self.solution_text, (10, 60), self.font, self.font_scale, self.font_color, self.line_type)
        cv2.putText(self.frame, self.front_text, (10, 120), self.font, self.font_scale, self.font_color, self.line_type)
        cv2.putText(self.frame, self.right_text, (10, 150), self.font, self.font_scale, self.font_color, self.line_type)
        cv2.putText(self.frame, self.left_text, (10, 180), self.font, self.font_scale, self.font_color, self.line_type)
        cv2.putText(self.frame, self.up_text, (10, 210), self.font, self.font_scale, self.font_color, self.line_type)
        cv2.putText(self.frame, self.down_text, (10, 240), self.font, self.font_scale, self.font_color, self.line_type)
        cv2.putText(self.frame, self.back_text, (10, 270), self.font, self.font_scale, self.font_color, self.line_type)