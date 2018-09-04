"""Grid building functions."""


def initialize_grid(x=12, y=12):
    """Return a list of lists, which forms a grid."""

    if x < 7:
        x = 7
    if y < 7:
        y = 7

    x_list = []
    y_list = []

    for i in range(x):
        x_list.append("-")

    for i in range(y):
        y_list.append(x_list.copy())

    return y_list


def build_walls(grid):
    """Construct walls on all four sides."""
    for i in range(len(grid[0])):
        grid[0][i] = "W"
        grid[len(grid) - 1][i] = "W"

    for i in range(len(grid)):
        grid[i][0] = "W"
        grid[i][len(grid[i]) - 1] = "W"

    return grid
