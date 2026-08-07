class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i=0
        if not intervals:
            print("no interval")
            return [newInterval]
        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                continue
            if (intervals[i][0] <= newInterval[0] and intervals[i][1] >= newInterval[1]):
                print("engulfed case")
                return intervals
            if newInterval[0] >= intervals[i][0]:
                print("overlap case")
                intervals[i] = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
                break
            else:
                print("insert case")
                intervals.insert(i, newInterval)
                break
        if i == len(intervals)-1 : intervals += [newInterval]
        ans = []
        for i in intervals:
            if ans and ans[-1][1] >= i[0]:
                val = ans.pop()
                val = [val[0], max(val[1], i[1])]
                ans.append(val)
            else:
                ans.append(i)
            

        return ans
        