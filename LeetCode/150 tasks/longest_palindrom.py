class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""

        max_palindrome = ""

        for i in range(len(s)):
            odd_palindrome = self.expandAroundCenter(s, i, i)
            even_palindrome = self.expandAroundCenter(s, i, i + 1)

            longer_palindrome = odd_palindrome if len(odd_palindrome) > len(even_palindrome) else even_palindrome

            if len(longer_palindrome) > len(max_palindrome):
                max_palindrome = longer_palindrome

        return max_palindrome

    def expandAroundCenter(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1:right]

sol = Solution()
print(sol.longestPalindrome("abcddcbas"))