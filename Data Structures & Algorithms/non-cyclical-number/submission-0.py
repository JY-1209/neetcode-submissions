class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False
            
            seen.add(n)
            n = self.sumOfSquares(n)

        return True
    
    def sumOfSquares(self, n: int) -> int:
        sum = 0

        while n > 0:
            digit = (n % 10) ** 2
            n = n // 10
            sum += digit
        
        return sum
