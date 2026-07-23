class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        cur_min = float("inf")

        while l <= r:
            if nums[l] < nums[r]:
                cur_min = min(cur_min, nums[l])
                break

            mid = (l + r) // 2
            cur_min = min(nums[mid], cur_min)

            if nums[mid] < nums[l]:
                r = mid - 1
            else:
                l = mid + 1
        
        return cur_min
