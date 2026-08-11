class Solution:
    def reverseBits(self, n: int) -> int:
        i = n
        number = 0
        ind = 0
        while ind < 32:
            if i&1 : number += 1<<(31 - ind)
            i >>= 1
            ind +=1
        return number