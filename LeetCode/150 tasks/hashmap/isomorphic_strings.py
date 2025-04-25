class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        relation = dict()

        for ss, tt in zip(s,t):

            if not relation.get(ss):
                relation[ss] = tt

            elif not relation[ss] == tt:
                return False

        relation = dict()
        for ss, tt in zip(t,s):

            if not relation.get(ss):
                relation[ss] = tt

            elif not relation[ss] == tt:
                return False


        return True

sol = Solution()
res = sol.isIsomorphic(s = "paper", t = "title")
print(res)
