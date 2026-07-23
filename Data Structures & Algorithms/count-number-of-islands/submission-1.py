class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        visited = set()
        islands = 0
        queue = collections.deque()

        def bfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return

            if (row, col) in visited:
                return

            visited.add((row, col))
            queue.append((row, col))

            while queue:
                node = queue.popleft()

                for dir in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                    new_row, new_col = dir[0] + node[0], dir[1] + node[1]
                    
                    if new_row not in range(rows) or new_col not in range(cols) or (new_row, new_col) in visited or grid[new_row][new_col] == "0":
                        continue

                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))
            

        for row in range(rows):
            for col in range(cols):
                if (row, col) in visited:
                    continue

                if grid[row][col] == "1":
                    bfs(row, col)
                    islands += 1
                    
                
        return islands
        