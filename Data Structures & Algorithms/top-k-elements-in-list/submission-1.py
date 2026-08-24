class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        arr = []

        for num, cnt in counts.items():
            arr.append((num, cnt))

        arr.sort(key=lambda x: x[1], reverse=True)

        return [num for num, cnt in arr[:k]]
