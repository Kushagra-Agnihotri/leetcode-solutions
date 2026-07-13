class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(i, current):
            if i >= n:
                if current not in res:
                    res.append(current)
                return 
            for j in range(len(current)+1):
                current = current[:j] + "()" + current[j:]
                dfs(i+1, current)
                current = current[:j] + current[j+2:]
        dfs(0,"")
        return res