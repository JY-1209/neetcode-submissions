class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        rows, cols = len(heights), len(heights[0])

        res = []

        def dfs(row, col, visited, prev_height):
            if row >= rows or col >= cols or row < 0 or col < 0 or heights[row][col] < prev_height or (row, col) in visited:
                return

            visited.add((row, col))

            dfs(row - 1, col, visited, heights[row][col])
            dfs(row + 1, col, visited, heights[row][col])
            dfs(row, col - 1, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])
        
        for col in range(cols):
            dfs(0, col, pac, heights[0][col])
            dfs(rows - 1, col, atl, heights[rows - 1][col])
        
        for row in range(rows):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, cols - 1, atl, heights[row][cols - 1])
        
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pac and (row, col) in atl:
                    res.append((row, col))
            
        return res