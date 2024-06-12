#!/usr/bin/env python3

import cv2

import cube.Cube as Cube

class DisplaySquare:
    """
    Display squares on the webcam feed.
    """

    def __init__(self, frame, color: tuple, pos: tuple):
        self.frame = frame
        self.size = 10
        self.thickness = -1
        self.color = color
        self.pos = pos

    def draw(self) -> None:
        """
        Draw the squares on the webcam feed.

        Parameters:
        - width (int): The width of the webcam feed.
        - height (int): The height of the webcam feed.

        Returns:
        - None
        """
        default_top_left_corner = (self.pos[0] / 2 - self.size * 1.5, self.pos[1] / 2 - self.size * 1.5)
        cv2.rectangle(self.frame, (int(default_top_left_corner[0]), int(default_top_left_corner[1])), (int(default_top_left_corner[0] + self.size * 3), int(default_top_left_corner[1] + self.size * 3)), self.color, self.thickness)



class SquaresManager:
    """
    Manage the squares on the webcam feed.
    """

    def __init__(self, frame, cube):
        self.frame = frame
        self.squares = []
        self.cube = cube


    def manage_squares(self) -> None:
        """
        Manage the squares on the webcam feed.
        """

        self.squares = []

        # FRONT FACE
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.FRONT, 0), (260, 1110)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.FRONT, 1), (330, 1110)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.FRONT, 2), (400, 1110)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.FRONT, 3), (260, 1180)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.FRONT, 4), (330, 1180)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.FRONT, 5), (400, 1180)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.FRONT, 6), (260, 1250)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.FRONT, 7), (330, 1250)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.FRONT, 8), (400, 1250)))

        # RIGHT FACE
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.RIGHT, 0), (470, 1110)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.RIGHT, 1), (540, 1110)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.RIGHT, 2), (610, 1110)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.RIGHT, 3), (470, 1180)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.RIGHT, 4), (540, 1180)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.RIGHT, 5), (610, 1180)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.RIGHT, 6), (470, 1250)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.RIGHT, 7), (540, 1250)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.RIGHT, 8), (610, 1250)))

        # LEFT FACE
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.LEFT, 0), (50, 1110)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.LEFT, 1), (120, 1110)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.LEFT, 2), (190, 1110)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.LEFT, 3), (50, 1180)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.LEFT, 4), (120, 1180)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.LEFT, 5), (190, 1180)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.LEFT, 6), (50, 1250)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.LEFT, 7), (120, 1250)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.LEFT, 8), (190, 1250)))

        # UP FACE
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.UP, 0), (260, 900)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.UP, 1), (330, 900)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.UP, 2), (400, 900)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.UP, 3), (260, 970)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.UP, 4), (330, 970)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.UP, 5), (400, 970)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.UP, 6), (260, 1040)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.UP, 7), (330, 1040)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.UP, 8), (400, 1040)))

        # DOWN FACE
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.DOWN, 0), (260, 1320)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.DOWN, 1), (330, 1320)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.DOWN, 2), (400, 1320)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.DOWN, 3), (260, 1390)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.DOWN, 4), (330, 1390)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.DOWN, 5), (400, 1390)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.DOWN, 6), (260, 1460)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.DOWN, 7), (330, 1460)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.DOWN, 8), (400, 1460)))

        # BACK FACE
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.BACK, 0), (680, 1110)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.BACK, 1), (750, 1110)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.BACK, 2), (820, 1110)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.BACK, 3), (680, 1180)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.BACK, 4), (750, 1180)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.BACK, 5), (820, 1180)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.BACK, 6), (680, 1250)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.BACK, 7), (750, 1250)))
        self.squares.append(DisplaySquare(self.frame, self.color_parser(Cube.Cube.BACK, 8), (820, 1250)))


    def color_parser(self, face, index) -> tuple:
        """
        Parse the colors of the squares.

        Parameters:
        - face (int): The face of the cube.
        - index (int): The index of the square.

        Returns:
        - tuple: The parsed colors of the squares.
        """

        if self.cube.faces[face][index] == "X":
            return (0, 0, 0)
        elif self.cube.faces[face][index] == "W":
            return (255, 255, 255)
        elif self.cube.faces[face][index] == "Y":
            return (0, 255, 255)
        elif self.cube.faces[face][index] == "B":
            return (255, 0, 0)
        elif self.cube.faces[face][index] == "G":
            return (0, 255, 0)
        elif self.cube.faces[face][index] == "R":
            return (0, 0, 255)
        elif self.cube.faces[face][index] == "O":
            return (255, 0, 255)


    def draw(self) -> None:
        """
        Draw the squares on the webcam feed.

        Returns:
        - None
        """

        self.manage_squares()
        for square in self.squares:
            square.draw()

