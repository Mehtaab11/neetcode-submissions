class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        idx = [-1] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
                idx[i] = stack[-1]
            else:
                idx[i] = i
            stack.append(i)

        res = [0] * n

        for i in range(n):
                res[i] = idx[i] - i

        return res
