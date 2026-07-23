class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_ptr = 0
        right_ptr = len(s) - 1

        s = s.lower()

        while right_ptr > left_ptr:
            if not s[left_ptr].isalnum():
                left_ptr += 1
                continue
            if not s[right_ptr].isalnum():
                right_ptr -= 1
                continue
            if s[left_ptr] == s[right_ptr]:
                left_ptr += 1
                right_ptr -= 1
            else:
                return False

        return True