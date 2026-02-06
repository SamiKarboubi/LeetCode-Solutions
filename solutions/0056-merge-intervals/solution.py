class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        result = []
        start, end = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] > end:
                result.append([start, end])
                start, end = intervals[i]
            else:
                end = max(end, intervals[i][1])

        result.append([start, end])
        return result
