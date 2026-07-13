class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def rec(i, current):
            nonlocal res
            print(i, current)
            if i== len(nums):
                res.append(current.copy())

                return 
            for j in range(len(current)+1):
                print(j)
                current.insert(j, nums[i])
                rec(i+1, current)
                current.pop(j)
        rec(1,[nums[0]])
        return res

