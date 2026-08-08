class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""

        for i in range(len(s)):
            for j in range(len(s) - 1, i - 1, -1):
                substring = s[i:j + 1]

                if substring == substring[::-1]:
                    if len(substring) > len(longest):
                        longest = substring

        return longest