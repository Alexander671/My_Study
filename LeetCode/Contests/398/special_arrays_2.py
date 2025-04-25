class Solution:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        lst = []
        for i in range(len(nums) - 1):
            if nums[i] % 2 == 0 and nums[i + 1] % 2 == 0 or nums[i] % 2 == 1 and nums[i + 1] % 2 == 1:
                lst.append(False)
            else:
                lst.append(True)


        prefix_sum = [0]
        for i in range(len(lst)):
            prefix_sum.append(prefix_sum[i] + lst[i])


        result = []
        for q in queries:
            if q[1] - q[0] == prefix_sum[q[1]] - prefix_sum[q[0]]:
                result.append(True)
            else:
                result.append(False)

        return result

sol = Solution()
print(sol.isArraySpecial(nums = [3,4,1,2,6], queries = [[0,4]]))
print(sol.isArraySpecial(nums = [4,3,1,6], queries = [[0,2],[2,3]]))
print(sol.isArraySpecial(nums = [2,1,2,2,1,2,2,2,1,2], queries = [[3,8]]))
