class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sub = []
        ans = []

        def backtrack():
            if len(nums) == len(sub):
                ans.append(sub[:])
                return

            for num in nums:
                if num in sub:
                    continue
                
                sub.append(num)
                backtrack()

                sub.pop()
        backtrack()
        return ans
