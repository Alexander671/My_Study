class Solution:

    def isHappy(self, n: int) -> bool:
        acc = n
        old_but_gold = set()
        while n > 1:
            acc = 0
            while n != 0:
                acc += (n % 10) ** 2
                n = n // 10
            
            if acc in old_but_gold:
                return False
            old_but_gold.add(acc)
            n = acc
        return True

sol = Solution()
res = sol.isHappy(n = 2)
print(res)
