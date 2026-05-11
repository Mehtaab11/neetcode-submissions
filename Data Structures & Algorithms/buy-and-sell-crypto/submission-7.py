class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxi = 0
        l = 0
        r = 1

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r

            profit = prices[r] - prices[l]
            maxi = max(maxi, profit)

        return maxi
