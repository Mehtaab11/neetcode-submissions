class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l , r  = 0 , 1

        maxi = 0
        while l <=r and r < len(prices):
            if prices[l] >= prices[r]:
                l = r
            profit = prices[r] - prices[l]

            maxi = max(profit , maxi)

            r += 1

        return maxi
            