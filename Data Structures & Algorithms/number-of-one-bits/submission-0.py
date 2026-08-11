class Solution:
    def hammingWeight(self, n: int) -> int:
        x = n
        count =0
        while x:
            if x%2: count +=1

            x//=2
        return count 