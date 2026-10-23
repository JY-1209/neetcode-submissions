class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return

        stack = []

        for token in tokens:
            if token == "+":
                first = stack.pop()
                second = stack.pop()
                stack.append(first + second)
            elif token == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(second - first)
            elif token == "*":
                first = stack.pop()
                second = stack.pop()
                stack.append(first * second)
            elif token == "/":
                first = stack.pop()
                second = stack.pop()
                res = 0 if first == 0 else int(second / first)
                stack.append(res)
            else:
                stack.append(int(token))
        
        return stack.pop()


