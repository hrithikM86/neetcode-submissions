class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        r, profit = 0, 0

        while r < len(prices):
            l = min(l, prices[r])
            profit = max(profit, prices[r]-l)
            r+=1


        return profit

        