class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        d = dict()
        for i in range(len(nums)):
            if nums[i] in d:
                if abs(i - d[nums[i]]) <= k:
                    return True
                else:
                    d[nums[i]] = i    
            else:
                d[nums[i]] = i
        return False

sol = Solution()
print(sol.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))