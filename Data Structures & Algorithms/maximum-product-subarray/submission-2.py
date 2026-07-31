class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_num = cur_min = cur_max = nums[0]

        for num in nums[1:]:
            tmp = cur_min * num

            cur_min = min(cur_max * num, cur_min * num, num)
            cur_max = max(cur_max * num, tmp, num)
            max_num = max(cur_max, max_num)
        
        return max_num