# Four Knights Puzzle Solver

This repository contains a Python implementation of the A* search and Branch & Bound algorithms to solve the Four Knights Puzzle.

## Problem Description

The Four Knights Puzzle is a problem played on a 3x3 chess board. The initial state has two white knights at the bottom and two black knights at the top. The goal of the puzzle is to have the opposing knights switch sides. Knights move following the standard chess rules(two squares ahead in any direction, then one square left or right).

## Algorithms

Two search algorithms have been implemented to solve this problem:

- **A*Search Algorithm**: This algorithm uses a heuristic function, specifically the sum of the Manhattan distances from each knight to its goal position, to guide the search towards the goal.

- **Branch & Bound Algorithm**: This algorithm is a straightforward exhaustive search that does not use a heuristic to guide its search. Instead, it explores all possible states until it finds the goal.

## Usage

To run the program, use a Python 3 interpreter

## Results
The program prints out the minimum number of moves required to solve the puzzle, the number of nodes expanded during the search, and the time taken for each of the A* and Branch & Bound algorithms.






