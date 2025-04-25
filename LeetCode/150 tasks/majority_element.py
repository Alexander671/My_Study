class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq = dict()
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1

        return max(freq, key=freq.get)

sol = Solution()
res = sol.majorityElement([8,9,8,9,8])
print(res)
