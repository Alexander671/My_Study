class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        duplicates = set()
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in duplicates:
                del nums[i]
            else:
                duplicates.add(nums[i])
        return len(duplicates)

sol = Solution()
res = sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(res)
