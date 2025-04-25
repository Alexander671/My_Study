class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        value = None
        freq = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] != value:                
                freq = 1
            if nums[i] == value and freq > 2:
                del nums[i]
            else:
                value = nums[i]
                freq += 1

        return len(nums)

sol = Solution()
res = sol.removeDuplicates([0,0,1,1,1,1,2,3,3])
print(res)
