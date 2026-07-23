class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_multiple, zero_cnt = 1, 0

        for num in nums:
            if num:
                total_multiple *= num
            else:
                zero_cnt += 1

        outputs = [0] * len(nums)
        
        if zero_cnt > 1:
            return outputs

        for i in range(len(nums)):
            if nums[i] == 0:
                outputs[i] = total_multiple
            else:
                outputs[i] = int(total_multiple / nums[i]) if not zero_cnt else 0
        
        return outputs