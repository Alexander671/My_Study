from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            sorted_str = ''.join(sorted(s))
            anagrams[sorted_str].append(s)
        return list(anagrams.values())

sol = Solution()
res = sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"])
print(res)
