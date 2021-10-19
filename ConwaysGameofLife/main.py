import random
import time


def check_neighbours(
    cells: dict, HEIGHT: int, WIDTH: int, ALIVE: str, DEAD: str
) -> dict:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            left = x - 1
            right = x + 1
            above = y - 1
            below = y + 1

            numNeighbours = 0
            if cells.get((left, above)) == ALIVE:
                numNeighbours += 1
            if cells.get((left, y)) == ALIVE:
                numNeighbours += 1
            if cells.get((left, below)) == ALIVE:
                numNeighbours += 1
            if cells.get((x, below)) == ALIVE:
                numNeighbours += 1
            if cells.get((right, below)) == ALIVE:
                numNeighbours += 1
            if cells.get((right, y)) == ALIVE:
                numNeighbours += 1
            if cells.get((right, above)) == ALIVE:
                numNeighbours += 1
            if cells.get((x, above)) == ALIVE:
                numNeighbours += 1

            if cells[(x, y)] == ALIVE and numNeighbours not in (2, 3):
                cells[(x, y)] = DEAD
            elif cells[(x, y)] == DEAD and numNeighbours == 3:
                cells[(x, y)] = ALIVE

    return cells


def print_cell_generation(cells: dict, HEIGHT: int, WIDTH: int):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x, y)], end="")
        print()


def main():
    WIDTH = 70
    HEIGHT = 20
    ALIVE = "|"
    DEAD = "-"

    nextCells = {}

    for x in range(WIDTH):
        for y in range(HEIGHT):
            if random.randint(1, 10) < 4:
                nextCells[(x, y)] = ALIVE
            else:
                nextCells[(x, y)] = DEAD

    while True:
        print_cell_generation(nextCells, HEIGHT, WIDTH)
        nextCells = check_neighbours(nextCells, HEIGHT, WIDTH, ALIVE, DEAD)
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            exit()


if __name__ == "__main__":
    main()
