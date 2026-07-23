class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[-1] * n for _ in range(m)]

        def dfs(row, col):
            if row == m - 1 and col == n - 1:
                return 1
            
            if row >= m or col >= n:
                return 0

            if cache[row][col] != -1:
                return cache[row][col]
            
            cache[row][col] = dfs(row, col + 1) + dfs(row + 1, col)
            return cache[row][col]

        return dfs(0, 0)