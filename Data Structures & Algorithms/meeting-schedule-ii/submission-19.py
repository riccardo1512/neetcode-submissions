"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x : (x.start, x.end))
        minHeap = []

        for i in intervals:
            start, end = i.start, i.end

            if minHeap and start >= minHeap[0]:
                heapq.heappop(minHeap)

            heapq.heappush(minHeap, end)

        return len(minHeap)
        