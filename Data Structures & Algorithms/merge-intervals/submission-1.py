class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        output = [intervals[0]]


        for interval in intervals:
            start, end = interval

            if output[-1][1] >= start:
                output[-1][1] = max(end , output[-1][1])
            else:
                output.append(interval)
        return output