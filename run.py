"""Main run process."""
import grid_builder as gb


def main():
    """Runtime."""
    grid = gb.initialize_grid(15, 15)
    grid = gb.build_walls(grid)

    for row in grid:
        print (row)


if __name__ == "__main__":
    main()
