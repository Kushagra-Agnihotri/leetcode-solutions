class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() if (c.isalnum()) else "" for c in s)
        print(s)
        return s == s[::-1]