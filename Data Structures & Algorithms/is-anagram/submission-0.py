class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_bank = {}
        t_bank = {}

        for char in s:
            s_bank[char] = 0 if char not in s_bank else s_bank[char] + 1
        
        for char in t:
            t_bank[char] = 0 if char not in t_bank else t_bank[char] + 1

        return s_bank == t_bank