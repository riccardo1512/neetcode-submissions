"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x : x.start)
        res = 0
        heap = [intervals[0].end]

        for i in intervals[1:]:
            if heap and heap[0] <= i.start:
                heapq.heappop(heap)
            heapq.heappush(heap, i.end)
        return len(heap)

        