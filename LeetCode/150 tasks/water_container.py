# height = [1,8,6,2,5,4,8,3,7]
# 
class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_v = 0
        l, r = 0, len(height) - 1
        while l < r:
            vol = min(height[l], height[r]) * (r - l)
            if vol > max_v:
                max_v = vol

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
        return max_v

sol = Solution()
print(sol.maxArea([1,3,2,5,25,24,5]))