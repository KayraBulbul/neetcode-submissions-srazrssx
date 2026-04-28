class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0

        for i in range(len(prices)):
            if right > len(prices) - 1:
                break
            else:
                if prices[right] < prices[left]:
                    left = right
                    right += 1
                else:
                    profit = max(profit, prices[right] - prices[left])
                    right += 1
        return profit