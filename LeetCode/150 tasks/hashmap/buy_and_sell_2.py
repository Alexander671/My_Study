class Solution:
    def maxProfit(self, prices):
        mi, ma = float('inf'), 0
        profit = 0
        i = 0
        d = 0

        while i != len(prices):
            p = prices[i]
            if p < mi and d == 0:
                mi = p
                i += 1

            elif p < prices[i-1] and d != 0:
                mi = float('inf')
                d = 0
                profit += ma

            elif p > mi:
                ma = p - mi
                d += 1
                i += 1

        profit += ma
        return profit


sol = Solution()
print(sol.maxProfit([1,2,3,4,5]))