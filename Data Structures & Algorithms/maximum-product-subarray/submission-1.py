class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = cur_max = cur_min = nums[0]

        for num in nums[1:]:
            tmp = cur_max * num
            cur_max = max(num, tmp, cur_min * num)
            cur_min = min(num, cur_min * num, tmp)
            max_product = max(cur_max, max_product)
        
        return max_product