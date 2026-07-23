class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def dfs(row, col):
            if row == m - 1 and col == n - 1:
                return 1
            if row >= m or col >= n:
                return 0

            return dfs(row, col + 1) + dfs(row + 1, col)

        return dfs(0, 0)