#!/usr/bin/python3
"""
Island Perimeter Calculation
"""

def island_perimeter(grid):
    """
    Calculates the perimeter of an island in a grid.

    Args:
        grid (list of list of int): 2D grid representing the map of the island

    Returns:
        int: Perimeter of the island
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # land cell
                perimeter += 4  # each land cell contributes 4 to the perimeter initially

                # Check adjacent cells (up, down, left, right) to reduce perimeter where there are neighboring land cells

                # Check above
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                # Check left
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter