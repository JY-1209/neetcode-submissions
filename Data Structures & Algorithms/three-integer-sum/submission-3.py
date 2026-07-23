class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        prev = None

        for i in range(len(nums)):
            if nums[i] == prev:
                continue

            remainder = 0 - nums[i]

            count = set()
            good_nums = set()

            for j in range(i + 1, len(nums)):
                if nums[j] in good_nums:
                    continue

                second_remainder = remainder - nums[j]

                if second_remainder in count:
                    good_nums.add(nums[j])
                    res.append([nums[i], nums[j], second_remainder])
                else:
                    count.add(nums[j])


            prev = nums[i]
        
        return res