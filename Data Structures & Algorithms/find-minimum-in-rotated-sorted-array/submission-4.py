class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        min_value = nums[0]

        while l <= r:
            mid = (l + r) // 2

            # left half is sorted
            if nums[l] <= nums[mid]:
                min_value = min(min_value, nums[l])
                l = mid + 1
            # right half is sorted
            else:
                min_value = min(min_value, nums[mid])
                r = mid - 1
        
        return min_value