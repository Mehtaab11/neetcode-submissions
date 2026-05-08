class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l, r = 0, 1

        maxi = 0
        for r in range(len(prices)):
            if prices[l] >= prices[r]:
                l = r
            profit = prices[r] - prices[l]
            maxi = max(prices[r] - prices[l], maxi)

        return maxi
