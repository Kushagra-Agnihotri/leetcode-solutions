class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2":"abc", 
                "3":"def", 
                "4":"ghi",
                "5":"jkl",
                "6":"mno",
                "7":"pqrs",
                "8":"tuv",
                "9":"wxyz"}
        res = []
        def dfs(i, current):
            if i>= len(digits):
                res.append(current)
                return 
            
            for j in mapping[digits[i]]:
                dfs(i+1, current+j)
        if digits:        
             dfs(0, "")             
        return res
