class Solution:
    def hammingWeight(self, x: int) -> int:
        count =0
        while x:
            if x&1 : count +=1
            x = x >> 1
        return count 