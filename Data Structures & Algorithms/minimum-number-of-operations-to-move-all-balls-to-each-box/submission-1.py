class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ones = []
        for i in range(len(boxes)):
            if boxes[i] == '1': ones.append(i)
        #print(ones)
        res = []
        for i, box in enumerate(boxes):
            t = 0
            
            for ind in ones:
                ind = int(ind)
                #rint(i, ind)
                if ind == i: continue
                t += abs(i-ind)
            res.append(t)
        return res