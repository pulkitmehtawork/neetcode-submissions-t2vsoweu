class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()


        prevEnd = intervals[0][1]
        res = 0
        for interval in intervals[1:]:
            start , end = interval
            if start >= prevEnd:
                 prevEnd = end
            else:
                res +=1
                prevEnd = min(end , prevEnd)
        return res