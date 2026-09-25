class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0

        intervals.sort()
        lastStart, lastEnd = intervals[0][0], intervals[0][1]
        for start, end in intervals[1:]:
            if start < lastEnd and end > lastEnd:
                res += 1
            elif start < lastEnd and end <= lastEnd:
                res += 1
                lastStart = start
                lastEnd = end
            else:
                lastStart = start
                lastEnd = end
        return res

        