class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = 0
        sold = len(prices) - 1
        max_difference = 0

        while prices[buy] != prices[sold]:
            if prices[buy] >= prices[sold]:
                buy -= 1
                continue

            if prices[buy] <= prices[sold]:
                if prices[sold] - prices[buy] > max_difference:
                    max_difference = prices[sold] - prices[buy]
                sold += 1

                
        return max_difference

sol = Solution()
res = sol.maxProfit([7,1,5,3,6,4])
print(res)