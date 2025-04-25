class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            if (value:=target - nums[i]) in nums[i+1:]:
                nums[i] = None
                return [i, nums.index(value)]


sol = Solution()
assert sol.twoSum(nums = [2,7,11,15], target = 9) ==  [0,1], sol.twoSum(nums = [2,7,11,15], target = 9)
assert sol.twoSum(nums = [3,2,4], target = 6) == [1,2], sol.twoSum(nums = [3,2,4], target = 6)
assert sol.twoSum(nums = [3,3], target = 6) == [0,1],  sol.twoSum(nums = [3,3], target = 6) 

