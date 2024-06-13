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
        else:
            if self.solver.moves != []:
                cv2.putText(self.frame, "### MOVES ###", (1500, 30), self.font, self.font_scale, self.font_color, self.line_type)
                for i in range(0, len(self.solver.moves), 5):
                    moves = ' '.join(self.solver.moves[i:i+5])
                    line_number = i // 5
                    cv2.putText(self.frame, moves, (1500, 70 + line_number * 40), self.font, self.font_scale, self.font_color, self.line_type)
            else:
                cv2.putText(self.frame, self.intro_text, (1200, 30), self.font, self.font_scale, self.font_color, self.line_type)
