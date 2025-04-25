from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


sol = Solution()
res = sol.isAnagram(s = "anagram", t = "nagaram")
print(res)