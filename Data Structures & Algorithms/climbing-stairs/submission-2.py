class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        first, second = 0, 1

        for i in range(2, n + 2):
            temp = first
            first = second
            second = second + temp
            print(first, second)

        return second