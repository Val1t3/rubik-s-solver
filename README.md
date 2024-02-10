# ResolveRubik-s

<img src="./assets/rubik&apos;s-cube.png" width="500" />

This repository implements a 3x3x3 Rubik's Cube solver using the Kociemba algorithm. The Kociemba algorithm is a two-phase algorithm that is widely used to solve the Rubik's Cube. The algorithm is based on the concept of God's number, which is the minimum number of moves required to solve the Rubik's Cube from any given position. The Kociemba algorithm is able to solve the Rubik's Cube in 20 moves or less, which is the current known upper bound for God's number.

## Getting Started

A 'launch.sh' file is provided to compile and run the program. The program can be run by executing the following command too:

```bash
./launch.sh
```

## Prerequisites

The following packages are required to run the program:

```
opencv-python
kociemba
```

These packages are in the requirements.txt file. You can install them by running the following command:

```bash
pip3 install -r requirements.txt
```

## Usage

The program can be run by executing the following command:

```bash
python3 src/main.py
```

The program will launch webcam to beginning to scan the Rubik's Cube. User need to
scan every face of the Rubik's Cube:

```bash
1 - Front
2 - Right
3 - Left
4 - Up
5 - Down
6 - back

a - solve Rubik's Cube
```

Help can be found by executing the following command:

```bash
python3 src/main.py -h
```

## Author
[Valentin Woehrel](https://github.com/Val1t3)