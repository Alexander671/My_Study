class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = dict()
        for note in magazine:
            freq[note] = freq.get(note, 0) + 1

        for i in range(len(ransomNote) -1, -1, -1):
            if ransomNote[i] in freq and ransomNote.count(ransomNote[i]) <= freq[ransomNote[i]]:
                continue
            else:
                return False

        return True

sol = Solution()
res = sol.canConstruct(ransomNote = "aa", magazine = "aab")
print(res)