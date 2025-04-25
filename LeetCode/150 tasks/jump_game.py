class Solution:

    def canJump(self, nums: list[int]) -> bool:

        i = 0
        while nums[i] + i + 1 < len(nums):

            if nums[i] == 0:
                return False

            ma_ndx = 0
            ma_value = 0

            for j in range(i, i + nums[i-1]):
                if nums[j] + j >= ma_value:
                    ma_ndx = j
                    ma_value = nums[j] + j
            i = ma_ndx
        return True

sol = Solution()
print(sol.canJump([2,3,1,1,4]))