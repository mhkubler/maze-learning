import random

from .maze import Maze


def generate_maze(width: int, height: int, seed=None):
    maze = Maze(width, height)
    rng = random.Random(seed)

    start: tuple[int, int] = (0, 0)
    visited: set[tuple[int, int]] = {start}
    stack: list[tuple[int, int]] = [start]

    while stack:
        current = stack[-1]

        unvisited = [
            neighbor
            for neighbor in maze.grid_neighbors(current)
            if neighbor not in visited
        ]

        if unvisited:
            next_node = rng.choice(unvisited)

            maze.connect(current, next_node)
            visited.add(next_node)
            stack.append(next_node)
        else:
            stack.pop()

    return maze

if __name__ == "__main__":
    maze = generate_maze(10, 10, seed=42)
    print(maze.passages)