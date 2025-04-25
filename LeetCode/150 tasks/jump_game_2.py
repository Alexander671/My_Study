class Solution:
    def find_max(self, nums, i):
        ma_ndx = 0
        ma_value = 0

        for j in range(i, i + nums[i-1]):
            if nums[j] + j >= ma_value:
                ma_ndx = j
                ma_value = nums[j] + j

        return ma_ndx

    def jump(self, nums: list[int]) -> bool:

        i = 0
        k = 0
        if len(nums) <= 1:
            return 0
        while nums[i] + i + 1 < len(nums):
            k += 1

            i = self.find_max(nums, i+1)

        return k + 1

sol = Solution()
print(sol.jump([2,3,1,1,4]))