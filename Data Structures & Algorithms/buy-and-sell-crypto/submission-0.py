class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = i = 0
        for j in range(1, len(prices)):
            if prices[j] < prices[i]:
                i = j
            else:
                res = max(res, prices[j] - prices[i])
        return res