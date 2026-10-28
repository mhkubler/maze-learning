from collections import deque

def bfs(maze, start, goal):
    passages = maze.passages

    if start == goal:
        return [start]

    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]
        if node not in visited:
            neighbours = passages[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
            visited.add(node)

    return None