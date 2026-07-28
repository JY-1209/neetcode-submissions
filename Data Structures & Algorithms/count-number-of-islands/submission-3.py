class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        visited = set()
        islands = 0

        def bfs(row, col):
            queue = collections.deque()

            if (row, col) in visited:
                return

            visited.add((row, col))
            queue.append((row, col))

            while queue:
                idx = queue.popleft()
                
                for direction in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    new_row, new_col = idx[0] + direction[0], idx[1] + direction[1]

                    if not (0 <= new_row < rows) or not (0 <= new_col < cols):
                        continue

                    if (new_row, new_col) in visited:
                        continue
                    
                    if grid[new_row][new_col] == "0":
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