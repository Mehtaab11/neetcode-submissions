class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        res = [0] * n
        stack = []

        for i in range(n-1, -1,-1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if stack:
                res[i] = stack[-1]

            stack.append(i)

        ans = [0] *n

        for i in range(n):
            if res[i] == 0:
                continue
                
            ans[i] = res[i] - i

        return ans