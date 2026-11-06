class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}
        l = 0
        max_chars = 0
        res = 0

        for r in range(len(s)):
            char_count[s[r]] = 1 + char_count.get(s[r], 0)
            max_chars = max(max_chars, char_count[s[r]])

            if (r - l + 1) - max_chars > k:
                char_count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

