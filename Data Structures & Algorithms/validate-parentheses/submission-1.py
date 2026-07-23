class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            elif c == ")":
                if len(stack) == 0 or stack[-1] != "(":
                    return False
                else:
                    stack.pop(-1)
            elif c == "}":
                if len(stack) == 0 or stack[-1] != "{":
                    return False
                else:
                    stack.pop(-1)
            elif c == "]":
                if len(stack) == 0 or stack[-1] != "[":
                    return False
                else:
                    stack.pop(-1)
        
        return len(stack) == 0
