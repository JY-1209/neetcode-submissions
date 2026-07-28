class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = longest_substring = 0
        unique_chars = set()

        for r in range(0, len(s)):
            while s[r] in unique_chars:
                unique_chars.remove(s[l])
                l += 1
            
            unique_chars.add(s[r])

            longest_substring = max(longest_substring, r - l + 1)

        return longest_substring
