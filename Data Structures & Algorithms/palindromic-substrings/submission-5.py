class Solution:
    def countSubstrings(self, s: str) -> int:
        count = len(s)
        #odd length 
        i = 0
        while i<len(s):
            r, l = i+1 , i-1
            if l<0 or r>=len(s):
                i+=1 
                continue

            while l >= 0 and  r < len(s) and s[l] == s[r]:
                count +=1
                # print(i, l ,r,"count" , count)
                
                r+=1
                l-=1
            i+=1
        #even length
        i = 0
        while i<len(s)-1:
            if s[i] == s[i+1]:
                
                count +=1
                l= i-1
                r= i+2
                while l>=0 and r<len(s) and s[l] == s[r]:
                    count +=1
                    # print(i, l ,r,"count" , count)

                    
                    l-=1
                    r+=1
            i+=1
        return count



