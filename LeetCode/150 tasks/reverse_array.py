class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k >= 1 and len(nums) > 1:
            nums[:] = (nums[-(k%len(nums)):] + nums[:len(nums) - k%len(nums)])[:len(nums)]

        return nums

sol = Solution()
res = sol.rotate(nums = [1,2], k = 2)
print(res)