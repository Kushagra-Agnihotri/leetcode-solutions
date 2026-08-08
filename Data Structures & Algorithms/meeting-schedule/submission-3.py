"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        # This pairs (intrvl 0, intrvl 1), (intrvl 1, intrvl 2), etc.
        for prev, curr in zip(intervals, intervals[1:]):
            if curr.start < prev.end:
                return False
        return True