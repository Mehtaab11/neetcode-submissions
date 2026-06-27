class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "+-/*":
                stack.append(int(token))

            if token == "+":
                num1, num2 = stack.pop(), stack.pop()
                res = num1 + num2

                stack.append(res)
            elif token == "-":
                num1, num2 = stack.pop(), stack.pop()
                res = num2 - num1

                stack.append(res)
            elif token == "/":
                num1, num2 = stack.pop(), stack.pop()
                res = int(num2 / num1)
                stack.append(res)
            elif token == "*":
                num1, num2 = stack.pop(), stack.pop()
                res = num1 * num2
                stack.append(res)

        return stack[-1]
