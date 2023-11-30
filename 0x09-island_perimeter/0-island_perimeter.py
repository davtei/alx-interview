#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """ returns the perimeter of the island described in grid """
    perimeter = 0
    for row, row_data in enumerate(grid):
        for col, cell in enumerate(row_data):
            if cell == 1:
                perimeter += 4
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2
    return perimeter
