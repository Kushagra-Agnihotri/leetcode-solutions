class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        pre , suf = [height[0]] , [height[-1]]
        for i in range(1,len( height)):
            pre.append(max(pre[-1], height[i]) )
            suf.append(max(suf[-1] , height[-1-i]))
        suf = suf[::-1]
        print(pre, suf)
        for i in range(len(height)):
            res += min(pre[i], suf[i])-height[i]
        return res