class Maze:
    def __init__(self, width: int, height: int):
        if width < 1 or height < 1:
            raise ValueError("maze dimensions must be positive")
        
        self.width = width
        self.height = height
        self.passages = {
            (row, col): []
            for row in range(height)
            for col in range(width)
        }

    def grid_neighbors(self, node):
        if node not in self.passages:
            raise ValueError("node is outside the maze")

        row, col = node
        candidates = [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1),
        ]

        return [
            neighbor
            for neighbor in candidates
            if neighbor in self.passages
        ]

    def connect(self, a, b):
        if b not in self.grid_neighbors(a):
            raise ValueError("nodes must be adjacent grid cells")

        if b not in self.passages[a]:
            self.passages[a].append(b)
            self.passages[b].append(a)

    def neighbors(self, node):
        if node not in self.passages:
            raise ValueError("node is outside the maze")

        return tuple(self.passages[node])