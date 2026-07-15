class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {2:"abc", 
                3:"def", 
                4:"ghi",
                5:"jkl",
                6:"mno",
                7:"pqrs",
                8:"tuv",
                9:"wxyz"}
        res = []
        current = ""
        if not digits:
            return  []
        def dfs(i):
            nonlocal current, res
            if len(current) == len(digits):
                res.append(current)
                return 
            digit  = int(digits[i])
            for j in range(len(mapping[digit])):
                current=current+mapping[digit][j]
                dfs(i+1)
                current = current[:-1]
        dfs(0)      

            
        return res
