class Solution:
    def maxProfit(self, prices):

        min_price = float("inf")
        max_profit = float("-inf")

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit


prices = [7, 1, 5, 3, 6, 4]

solution = Solution()
result = solution.maxProfit(prices)

print(result)
