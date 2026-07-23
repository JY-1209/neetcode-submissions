class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        prev = None

        for i in range(len(nums)):
            if nums[i] == prev:
                continue

            remainder = 0 - nums[i]

            seen = set()
            used = set()

            for j in range(i+1, len(nums)):
                if nums[j] in used:
                    continue

                zero_remainder = remainder - nums[j]

                if zero_remainder in seen:
                    res.append([nums[i], nums[j], zero_remainder])
                    used.add(nums[j])
                    used.add(zero_remainder)
                
                seen.add(nums[j])

            prev = nums[i]
        
        return res

                
