class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            stone_one = heapq.heappop_max(stones)
            stone_two = heapq.heappop_max(stones)

            if stone_one > stone_two:
                heapq.heappush_max(stones, stone_one - stone_two)
        
        return stones[0] if stones else 0