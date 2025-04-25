class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        count = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                del nums[i]
                nums.append(None)
            else:
                count += 1
        return count

sol = Solution()
res = sol.removeElement(nums = [0,1,2,2,3,0,4,2], val=2)
print(res)