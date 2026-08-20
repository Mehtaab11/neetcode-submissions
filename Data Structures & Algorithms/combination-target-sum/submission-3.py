class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []

        comb = []
        ans = []

        def CS(i, target):

            if target == 0:
                ans.append(comb[:])
                return

            if i == len(nums) or target < 0:
                return


            comb.append(nums[i])
            CS(i, target - nums[i])

            comb.pop()
            CS(i + 1, target)

        CS(0, target)
        return ans
