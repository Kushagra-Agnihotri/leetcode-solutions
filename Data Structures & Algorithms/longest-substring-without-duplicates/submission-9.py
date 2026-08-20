class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = len(set(list(s)))
        while letters>0:
            for i in range(len(s)-letters+1):
                window = set(list(s[i:i+letters]))
                if len(window) == letters:
                    return letters
            letters -= 1
        return len(set(list(s)))
        