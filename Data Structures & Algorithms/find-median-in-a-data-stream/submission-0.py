class MedianFinder:

    def __init__(self):
        self.datastream = []

    def addNum(self, num: int) -> None:
        self.datastream.append(num)


    def findMedian(self) -> float:
        n = len(self.datastream)
        arr = self.datastream
        arr.sort()
        return arr[n//2] if n % 2 else (arr[(n-1)//2] +arr[n//2])/2       