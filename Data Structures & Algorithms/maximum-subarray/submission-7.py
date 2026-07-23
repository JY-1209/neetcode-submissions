class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        max_sum = cur_sum = nums[0]

        for num in nums[1:]:
            # if num > cur_sum + num:
            #     cur_sum = num
            # else:
            #     cur_sum += num

            # max_sum = max(cur_sum, max_sum)
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)
        
        return max_sum
