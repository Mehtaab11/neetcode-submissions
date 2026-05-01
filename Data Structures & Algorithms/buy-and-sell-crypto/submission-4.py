class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l , r  = 0 , 1

        maxi = 0
        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
            profit = prices[r] - prices[l]
            maxi = max(prices[r] - prices[l] , maxi)

            r += 1

        return maxi
            