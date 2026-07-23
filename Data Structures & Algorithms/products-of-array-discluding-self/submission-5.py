class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_cnt = 0

        for num in nums:
            if num == 0:
                zero_cnt += 1
            else:
                total_product *= num

            if zero_cnt > 1:
                total_product = 0
                return [0] * len(nums)

        outputs = []

        if zero_cnt < 1:
            for num in nums:
                outputs.append((int(total_product / num)))
        elif zero_cnt == 1:
            for num in nums:
                if num == 0:
                    outputs.append(total_product)
                else:
                    outputs.append(0)

        return outputs