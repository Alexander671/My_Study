class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()

        if len(s) != len(pattern):
            return False

        relation = dict()

        for ss, tt in zip(pattern,s):

            if not relation.get(ss):
                relation[ss] = tt

            elif not relation[ss] == tt:
                return False

        relation = dict()
        for ss, tt in zip(s,pattern):

            if not relation.get(ss):
                relation[ss] = tt

            elif not relation[ss] == tt:
                return False


        return True


sol = Solution()
res = sol.wordPattern(pattern = "abba", s = "dog cat cat fish")
print(res)