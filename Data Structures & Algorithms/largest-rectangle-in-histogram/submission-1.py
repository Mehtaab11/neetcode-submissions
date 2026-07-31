class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack= []
        n = len(heights)

        maxi = 0

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:

                height = heights[stack.pop()]

                right= i

                left = stack[-1] if stack else -1

                width = right -left -1

                area = width * height

                maxi = max(maxi, area)
            
            stack.append(i)

        while stack:
        
            height = heights[stack.pop()]

            right= n

            left = stack[-1] if stack else -1

            width = right -left -1

            area = width * height

            maxi = max(maxi, area)
                

        return maxi