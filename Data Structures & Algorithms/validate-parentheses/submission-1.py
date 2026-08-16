class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        for bra in s:


            if stk and (bra == ")" and stk[-1] == "(" or 
                bra == "}" and stk[-1] == "{" or
                bra == "]" and stk[-1] == "[" ):
                stk.pop()
            else:
                stk.append(bra)
        return len(stk) == 0