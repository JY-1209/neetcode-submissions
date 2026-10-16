class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def dfs(i, end, memo):
            if i >= end:
                return 0

            if i in memo:
                return memo[i]

            skip = dfs(i + 1, end, memo)
            rob = nums[i] + dfs(i + 2, end, memo)

            memo[i] = max(skip, rob)
            return memo[i]

        return max(
            dfs(0, len(nums) - 1, {}),
            dfs(1, len(nums), {})
        )