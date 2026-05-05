class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)

        def nsl(heights):
            left = [-1] * n
            stack = []

            for i in range(n):
                while stack and heights[i] <= heights[stack[-1]]:
                    stack.pop()

                if stack :
                    left[i] = stack[-1]
                
                stack.append(i)
            return left


        def nsr(heights):
            right = [n] * n
            stack = []

            for i in range(n-1,-1,-1):
                while stack and heights[i] <= heights[stack[-1]]:
                    stack.pop()

                if stack :
                    right[i] = stack[-1]
                
                stack.append(i)
            return right


        # note : we are working with the index here not the value
        # note : because we are required to calculate the possible width 
        # note : which has nothing to do with the values

        right = nsr(heights)
        left = nsl(heights)

        max_area = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            area = width * heights[i]
            max_area = max(max_area, area)

        return max_area
