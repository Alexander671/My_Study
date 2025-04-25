# [100,4,200,1,3,2]
# acc = 1; value = 100; [100,4,200,1,3,2]
# 99 not in set; 101 not in set

# acc = 1; value = 2;
# values_before = 1; 1 in set; acc = 2; [100,4,200,3,2]
# values_before = 0; 0 not in set; acc = 2; [100,4,200,3,2]

# values_after = 3; 3 in set; acc = 3; [100,4,200,2]
# values_after = 4; 4 in set; acc = 4; [100,200,2]
# values_after = 5; 5 not in set; acc = 4; [100,200,2]




from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_dict = defaultdict(set)

        nums_set = set(nums)
        result_set = set()
        results = []

        for value in nums_set:
            acc = 1
            values_before, values_after = value, value

            if value in result_set:
                continue
            while (values_before:=values_before - 1) in nums_set:
                result_set.add(values_before)
                acc += 1

            while (values_after:=values_after + 1) in nums_set:
                result_set.add(values_after)
                acc += 1

            results.append(acc)

        return 0 if results == [] else max(results)

sol = Solution()
print(sol.longestConsecutive(nums =[-6,8,-5,7,-9,-1,-7,-6,-9,-7,5,7,-1,-8,-8,-2,0]))
print(sol.longestConsecutive(nums =[100,4,200,1,3,2]))