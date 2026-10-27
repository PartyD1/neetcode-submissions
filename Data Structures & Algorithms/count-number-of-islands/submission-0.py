
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total_count = 0
        q = deque()
        seen = set()
        maxRow = len(grid)
        maxCol = len(grid[0])

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    if (row, col) in seen:
                        continue
                    else:
                        seen.add((row, col))
                        q.append((row, col))

                        while q:
                            r, c = q.popleft()

                            # Up
                            if r != 0 and grid[r-1][c] == "1" and (r-1, c) not in seen:
                                q.append((r-1, c))
                                seen.add((r-1, c))

                            # Down
                            if r < maxRow - 1 and grid[r+1][c] == "1" and (r+1, c) not in seen:
                                q.append((r+1, c))
                                seen.add((r+1, c))

                            # Left
                            if c != 0 and grid[r][c-1] == "1" and (r, c-1) not in seen:
                                q.append((r, c-1))
                                seen.add((r, c-1))

                            # Right
                            if c < maxCol - 1 and grid[r][c+1] == "1" and (r, c+1) not in seen:
                                q.append((r, c+1))
                                seen.add((r, c+1))

                        total_count += 1


        return total_count
