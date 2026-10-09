class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1] * len(cost)

        def dfs(idx):
            if idx >= len(cost):
                return 0

            if memo[idx] != -1:
                return memo[idx]
            
            memo[idx] = cost[idx] + min(dfs(idx + 1), dfs(idx + 2))
            return memo[idx]
        
        return min(dfs(0), dfs(1))