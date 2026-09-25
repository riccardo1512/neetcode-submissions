"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x : x.start)

        prevEnd = -1
        for i in intervals:
            if i.start < prevEnd:
                return False
            prevEnd = i.end
        return True