class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_bank = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            char_bank[s[i]] = char_bank.get(s[i], 0) + 1
            char_bank[t[i]] = char_bank.get(t[i], 0) - 1

        return all(v == 0 for v in char_bank.values())