class Solution:

    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_sum_index = 500001
        prefix_sums = [0]
        min_sum = float('inf')

        for i in range(len(nums)):
            prefix_sums.append(nums[i] + prefix_sums[i])
        print(prefix_sums)
        for i in range(len(prefix_sums)):

            l = i
            r = len(prefix_sums) - 1

            while l < r:
                m = (l + r) // 2

                if (current_sum:=prefix_sums[m] - prefix_sums[i]) >= target:
                    print(i, m, current_sum)

                    if (current_sum <= min_sum) and ((m - i) <= min_sum_index):
                        min_sum_index = m - i
                        min_sum = current_sum
                        print(min_sum, min_sum_index)
                    r = m

                else:
                    print(i, m, current_sum)
                    l = m + 1

        return 0 if min_sum_index == 500001 else min_sum_index 


sol = Solution()
assert sol.minSubArrayLen(target = 4, nums = [1,4,4]) == 1
assert sol.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]) == 2
assert sol.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1]) == 0
assert sol.minSubArrayLen(15, [5,1,3,5,10,7,4,9,2,8]) == 2
assert sol.minSubArrayLen(11, [1,2,3,4,5]) == 2
