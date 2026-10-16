class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sums = []

        def dfs(i, visiting, total):
            if total > target or i >= len(nums):
                return

            if total == target:
                sums.append(visiting.copy())
                return
            
            visiting.append(nums[i])
            dfs(i, visiting, total + nums[i])
            visiting.pop()
            dfs(i + 1, visiting, total)
        
        dfs(0, [], 0)
        return sums