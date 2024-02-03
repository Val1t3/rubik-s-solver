#!/usr/bin/env python3

import cube.Cube as Cube

def main() -> None:
    cube = Cube.Cube()
    cube.faces[Cube.FRONT] = ["W" for _ in cube.faces[Cube.FRONT]]
    cube.faces[Cube.RIGHT] = ["G" for _ in cube.faces[Cube.RIGHT]]
    cube.faces[Cube.LEFT] = ["B" for _ in cube.faces[Cube.LEFT]]
    cube.faces[Cube.UP] = ["R" for _ in cube.faces[Cube.UP]]
    cube.faces[Cube.DOWN] = ["O" for _ in cube.faces[Cube.DOWN]]
    cube.faces[Cube.BACK] = ["Y" for _ in cube.faces[Cube.BACK]]
    print(cube)

if __name__ == "__main__":
    main()