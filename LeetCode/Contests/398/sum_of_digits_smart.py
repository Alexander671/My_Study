class Solution:
    def sumDigitDifferences(self, nums: list[int]) -> int:
        num_digits = len(str(nums[0]))
        n = len(nums)
        digit_positions = [[] for _ in range(num_digits)]

        for num in nums:
            num_str = str(num)
            for idx in range(num_digits):
                digit_positions[idx].append(int(num_str[idx]))
        
        total_differences = 0


        for digit_list in digit_positions:
            count = [0] * 10
            for digit in digit_list:
                count[digit] += 1

            for digit in range(10):
                total_differences += count[digit] * (n - count[digit])
        
        return total_differences // 2

sol = Solution()
print(sol.sumDigitDifferences(nums=[13, 23, 12]))  # Output: 4

sol = Solution()
print(sol.sumDigitDifferences(nums=[13, 23, 12]))  # Output: 4