class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = [intervals[0]]

        for s, e in intervals:
            last = res[-1][1]

            if last >= s:
                res[-1][1] = max(e, last)
            else:
                res.append([s, e])
        return res
    