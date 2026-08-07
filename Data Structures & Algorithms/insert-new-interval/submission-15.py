class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        if not intervals: return [newInterval]

        if intervals[0][0] > newInterval[1]:
            return [newInterval] +  intervals
        if intervals[-1][1] < newInterval[0]:
            return  intervals +[newInterval] 
        
        
        for i in range(len(intervals)):
            #print(i, newInterval, res)
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
                continue
            if intervals[i][0] > newInterval[1]:               
                res+= [newInterval] +intervals[i:]
                newInterval = []
                break
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        if newInterval: res+= [newInterval]
        
        return res if res else [newInterval]
            