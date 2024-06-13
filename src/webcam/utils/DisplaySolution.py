#!/usr/bin/env python3

import cv2

from algorithm.Solver import Solver
from cube import Cube

class DisplaySolution:
    def __init__(self, frame, cube: Cube, solver: Solver):
        self.frame = frame
        self.cube = cube
        self.solver = solver
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.font_scale = 1
        self.font_color = (0, 200, 0)
        self.line_type = 2
        self.error_text = "Cube doesn't completely scanned."
        self.intro_text = "Ready to solve the cube. Press 'a' to solve."


    def draw(self) -> None:
        if self.cube.contains_x():
            cv2.putText(self.frame, self.error_text, (1300, 30), self.font, self.font_scale, self.font_color, self.line_type)
        elif self.solver.moves == []:
            cv2.putText(self.frame, self.intro_text, (1200, 30), self.font, self.font_scale, self.font_color, self.line_type)
