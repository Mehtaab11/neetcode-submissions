class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        n = len(tokens)
        for token in tokens:
            if token == '+':
                rhs = stack.pop()
                lhs = stack.pop()
                res = lhs + rhs
                stack.append(res) 

            elif token == '-':
                rhs = stack.pop()
                lhs = stack.pop()
                res = lhs - rhs
                stack.append(res)
            elif token == '*':
                rhs = stack.pop()
                lhs = stack.pop()
                res = lhs * rhs
                stack.append(res)
            elif token == '/':
                rhs = stack.pop()
                lhs = stack.pop()
                res = int(lhs / rhs)
                stack.append(res)
            else:
                stack.append(int(token))

        return stack[-1]