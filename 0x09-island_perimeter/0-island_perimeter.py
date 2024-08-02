#!/usr/bin/python3
'''0x09. Island Perimeter'''


def island_perimeter(grid):
    '''Get the number of rows and columns in the grid'''
    num_rows = len(grid)
    num_cols = len(grid[0])

    # Initialize the perimeter counter
    perimeter = 0

    # Loop through each cell in the grid
    for row in range(num_rows):
        for col in range(num_cols):
            # Check if the current cell is land
            if grid[row][col] == 1:
                # Check the four possible sides of the land cell

                # Check the top side
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1

                # Check the bottom side
                if row == num_rows - 1 or grid[row + 1][col] == 0:
                    perimeter += 1

                # Check the left side
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1

                # Check the right side
                if col == num_cols - 1 or grid[row][col + 1] == 0:
                    perimeter += 1

    return perimeter
