""" A python script that runs Conway's Game of game_of_life

.. module:: game_of_life.py
    :platform: Windows, Unix
    :synopsis: This script receives as input a set of arguments to run the game of life.

.. moduleauthor:: Srijana Shrestha
        srijana.shrestha@wsu.edu

"""
from sys import argv

# print the grid
def print_grid(grid, rows, columns):
    """This function prints a grid of rows and columns.

    The first cell starts with cell index value [0,0]

    :param rows: no. of rows in the grid
    :type rows: an integer

    :param columns: no. of columns in the grid
    :type columns: an integer

    :return: A grid with given no. of rows and columns
    :type: A 2D array
    """

    # changing values from '0' to '-' and '1' to 'X' in the grid
    for i in range(rows):
        for j in range(columns):
            #print(grid[i][j], end = '')
            if grid[i][j] == 0:
                print("-", end = '')
            if grid[i][j] == 1:
                print("X", end = '')
        print()
    print()

#making a function to apply the rules
def apply_rules(grid, rows, columns):
    """This function applies the rules of game
    The number of live and dead cells are counted and added to decide the status of cell in the new grid.

    :param rows: the no. of rows in the grid
    :type rows: an integer

    :param columns: the bo. of columns in the grids
    :type columns: an integer

    :return: a new grid after applying the rules
    :type: A 2D array

    """
    # initialize the grid with the given cell indexes by users
    def initialize_grid(grid, cell_indexes):
        for cell_index in cell_indexes: # iterate through the cell indexes from user
            a = cell_index.split(':')
            grid[int(a[0]) - 1][int(a[1]) - 1] = 1

# Runs the program
def main():
    """This function runs the program

    Defines the script, no. of ticks provided by the user. It creates an empty
    grid with all 0's and then iterates through the cell indexes provided by
    user to turn the cell on by printing 'X.' For each tick, the new grid is
    printed with applied rules.

    :return: grid with applied rules
    :type: A 2D array

    """

    script = argv[0]
    ticks = argv[1]
    cell_indexes = argv[2:]

    #create an empty grid
    rows = 30
    columns = 80
    grid = [0] * rows
    for i in range(rows):
        grid[i] = [0] * columns

    #initialize the grid with the starting cells
    initialize_grid(grid, cell_indexes)

    #iterate through the ticks
    for tick in range(int(ticks)):
        print_grid(grid, rows, columns)

        #apply the rules (make a function)
        apply_rules(grid, rows, columns)

        # create a new grid
        new_grid = grid(rows, columns)

        #count neighbor cells
        for i in range(rows):
            for j in range(columns):
                nw = grid[i - 1][j - 1]
                n = grid[i - 1][j]
                w = grid[i][j - 1]

                if j == ncolumns - 1:
                    e = grid[i][j]
                else:
                    e = [i][j + 1]

                if j == columns - 1:
                        ne = grid[i-1][j]
                else:
                    ne = grid[i - 1, j + 1]

                if i == rows - 1:
                    sw = grid[i][j - 1]
                else:
                    sw = grid[i + 1] [j - 1]

                if i == rows - 1:
                    s = grid[i][j]
                else:
                    s = grid[i + 1] [j]


                # define neighbors
                neighbors = nw + n + ne + w + sw + s + se + e

                # set up new grid values
                new_grid[i][j] = grid[i][j]

                # apply changes to new_grid
                if grid[i][j] == 1:
                    if neighbors > 3:
                        new_grid[i][j] = 0
                    if neighbors < 2:
                        new_grid[i][j] = 0
                    if neighbors == 2 or neighbors == 3:
                        new_grid[i][j] = 1
                if grid[i][j] == 0:
                    if neighbors == 3:
                        new_grid[i][j] = 1
                    else:
                        new_grid[i][j] = 0

                return (new_grid)

                ntick = 1
                while ntick <= (int(ticks) + 1):

                    print_grid(grid, rows, columns)

                    apply_rules(grid, rows, columns)


# Call the main function
if __name__ =="__main__":
    main()
