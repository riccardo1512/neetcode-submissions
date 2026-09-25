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

        res = 0
        heap = []
        for i in intervals:
            heapq.heappush(heap, [i.start, True])
            heapq.heappush(heap, [i.end, False]) # (number : start/end)

        count = 0
        while heap:
            i = heapq.heappop(heap)
            if i[1]:
                count += 1
            else:
                count -= 1
            res = max(res, count)
        return res