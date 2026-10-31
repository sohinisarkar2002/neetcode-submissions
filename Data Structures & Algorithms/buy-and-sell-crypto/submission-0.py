class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        l = len(prices)

        left = 0
        right = 1

        while right < l:
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxi = max(profit, maxi)
            else:
                left = right

            right += 1

        return maxi