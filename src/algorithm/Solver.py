#!/usr/bin/env python3

from src.cube.Cube import Cube

import copy

class Solver:

    """
    Class to resolve the Rubik's Cube.
    """

    MOVEMENTS = [
        "U",
        "U'",
        "L",
        "L'",
        "R",
        "R'",
        "F",
        "F'",
        "B",
        "B'",
        "D",
        "D'"
    ]

    def __init__(self, cube: Cube) -> None:
        self.cube = cube
        self.moves = []


    def solve(self) -> None:
        print("\n### Solving... ###")
        res_moves = []

        # colors_list = self.colors_cube_to_list()
        # if not self.error_handling(colors_list):
        #     return

        # colors_str = self.format_colors(colors_list)
        # print(f"Cube string: {colors_str}")

        # Check for every piece of the FRONT face
        for i in range(len(self.cube.faces[Cube.FRONT])):
            if self.cube.faces[Cube.FRONT][i] != self.cube.faces[Cube.FRONT][4]:
                # try for 1 move, 2 moves, 3 moves...
                new_moves = self.check_one_rotation(self.cube.faces[Cube.FRONT][4], i)
                if not new_moves:
                    new_moves = self.check_two_rotations(self.cube.faces[Cube.FRONT][4], i)
                if not new_moves:
                    new_moves = self.check_three_rotations(self.cube.faces[Cube.FRONT][4], i)
                # do new_moves on cube.
                for move in new_moves:
                    self.cube.rotate(move)
                # add moves to res_moves.
                res_moves.extend(new_moves)
                self.cube.display_cube()

        print(f"Moves: {res_moves}")
        self.cube.display_cube()


    def check_one_rotation(self, color: chr, index: int) -> list:
        """
        Check for one rotation of the FRONT face.
        """

        res = []
        cube_tmp = copy.deepcopy(self.cube)

        # Check for one rotation
        for move in self.MOVEMENTS:
            cube_tmp.rotate(move)
            if cube_tmp.faces[Cube.FRONT][index] == color:
                mismatch_found = any(cube_tmp.faces[Cube.FRONT][i] != color and self.cube.faces[Cube.FRONT][i] == color for i in range(index))
                if not mismatch_found:
                    print(f"Found one rotation for {color} at index {index}.")
                    res.append(move)
                    break
            else:
                cube_tmp = copy.deepcopy(self.cube)

        return res


    def check_two_rotations(self, color: chr, index: int) -> list:
        """
        Check for two rotations of the FRONT face.
        """
        res = []
        cube_tmp = copy.deepcopy(self.cube)

        # Check for two rotations
        for move1 in self.MOVEMENTS:
            cube_tmp.rotate(move1)
            mismatch_found_1 = any(cube_tmp.faces[Cube.FRONT][i] != color and self.cube.faces[Cube.FRONT][i] == color for i in range(index))
            if mismatch_found_1:
                cube_tmp = copy.deepcopy(self.cube)
                continue
            for move2 in self.MOVEMENTS:
                cube_tmp.rotate(move2)
                if cube_tmp.faces[Cube.FRONT][index] == color:
                    mismatch_found_2 = any(cube_tmp.faces[Cube.FRONT][i] != color and self.cube.faces[Cube.FRONT][i] == color for i in range(index))
                    if not mismatch_found_2:
                        print(f"Found two rotations for {color} at index {index}: {move1}, {move2}")
                        res.extend([move1, move2])
                        break
                cube_tmp = copy.deepcopy(self.cube)  # Reset the cube to the state before move1
                cube_tmp.rotate(move1)  # Apply the first move again

            if res:
                break

            cube_tmp = copy.deepcopy(self.cube)  # Reset the cube if the combination of moves didn't work

        return res


    def check_three_rotations(self, color: chr, index: int) -> list:
        """
        Check for three rotations of the FRONT face.
        """
        res = []
        original_cube = copy.deepcopy(self.cube)

        # Check for three rotations
        for move1 in self.MOVEMENTS:
            self.cube.rotate(move1)
            mismatch_found_1 = any(self.cube.faces[Cube.FRONT][i] != color and original_cube.faces[Cube.FRONT][i] == color for i in range(index))
            if mismatch_found_1:
                self.cube = copy.deepcopy(original_cube)
                continue
            for move2 in self.MOVEMENTS:
                self.cube.rotate(move2)
                mismatch_found_2 = any(self.cube.faces[Cube.FRONT][i] != color and original_cube.faces[Cube.FRONT][i] == color for i in range(index))
                if mismatch_found_2:
                    self.cube = copy.deepcopy(original_cube)  # Reset the cube to the state before move1
                    self.cube.rotate(move1)  # Apply the first move again
                    continue
                for move3 in self.MOVEMENTS:
                    self.cube.rotate(move3)
                    if self.cube.faces[Cube.FRONT][index] == color:
                        mismatch_found_3 = any(self.cube.faces[Cube.FRONT][i] != color and original_cube.faces[Cube.FRONT][i] == color for i in range(index))
                        if not mismatch_found_3:
                            print(f"Found three rotations for {color} at index {index}: {move1}, {move2}, {move3}")
                            res.extend([move1, move2, move3])
                            break
                    self.cube = copy.deepcopy(original_cube)  # Reset the cube to the state before move1
                    self.cube.rotate(move1)  # Apply the first move again
                    self.cube.rotate(move2)  # Apply the second move again

                if res:
                    break

                self.cube = copy.deepcopy(original_cube)  # Reset the cube to the state before move1
                self.cube.rotate(move1)  # Apply the first move again

            if res:
                break

            self.cube = copy.deepcopy(original_cube)  # Reset the cube to the original state

        return res


    def error_handling(self, cube_str: str) -> bool:
        if len(cube_str) != 54:
            print("Error: The cube string must be 54 characters long.")
            return False

        # Check for correct center pieces
        center_pieces_indices = [4, 13, 22, 31, 40, 49]
        expected_centers = 'RGWOBY'
        for i, center in zip(center_pieces_indices, expected_centers):
            if cube_str[i] != center:
                print(f"Error: Center piece for {center} face is incorrect. Found {cube_str[i]}")
                return False

        # Check for correct count of each color
        for color in 'RGWOBY':
            count = cube_str.count(color)
            if count != 9:
                print(f"Error: Color {color} count mismatch. Found {count}, expected 9.")
                return False

        return True


    def colors_cube_to_list(self) -> list:
        colors_list = []
        colors_list.extend(self.cube.faces[Cube.UP])
        colors_list.extend(self.cube.get_face(Cube.FRONT))
        colors_list.extend(self.cube.get_face(Cube.RIGHT))
        colors_list.extend(self.cube.get_face(Cube.BACK))
        colors_list.extend(self.cube.get_face(Cube.LEFT))
        colors_list.extend(self.cube.get_face(Cube.DOWN))

        return colors_list


    def format_colors(self, colors: list) -> str:
        res = "".join(colors)
        res = res.replace("W", "F")
        res = res.replace("B", "L")
        res = res.replace("Y", "B")
        res = res.replace("R", "U")
        res = res.replace("G", "R")
        res = res.replace("O", "D")

        return res.lower()