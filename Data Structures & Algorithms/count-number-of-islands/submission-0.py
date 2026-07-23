class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        visited = set()
        islands = 0

        queue = collections.deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(row, col):
            if (row, col) in visited:
                return
            
            visited.add((row, col))
            queue.append((row, col))

            while queue:
                idx = queue.popleft()

                for direction in directions:
                    new_row, new_col = idx[0] + direction[0], idx[1] + direction[1]

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
                