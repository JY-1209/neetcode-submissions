class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_mapping = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        parentheses_stack = []

        for char in s:
            if char in parentheses_mapping.values():
                parentheses_stack.append(char)
            
            else:
                if len(parentheses_stack) == 0:
                    return False
                
                if parentheses_stack[-1] == parentheses_mapping[char]:
                    parentheses_stack.pop()
                else:
                    return False
        
        return len(parentheses_stack) == 0