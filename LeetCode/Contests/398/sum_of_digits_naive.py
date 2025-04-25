"""
Input: nums = [13,23,12]

Output: 4

Explanation:
We have the following:
- The digit difference between 13 and 23 is 1.
- The digit difference between 13 and 12 is 1.
- The digit difference between 23 and 12 is 2.
So the total sum of digit differences between all pairs of integers is 1 + 1 + 2 = 4.
"""

class Solution:
    def cipher_diff(self, x, y):
        acc = 0
        while x != 0:
            if x % 10 != y % 10:
                acc += 1
            x = x // 10
            y = y // 10
        return acc

    def sumDigitDifferences(self, nums: list[int]) -> int:
        sum = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum += self.cipher_diff(nums[i], nums[j])

        return sum

sol = Solution()
print(sol.sumDigitDifferences(nums = [13,23,12]))