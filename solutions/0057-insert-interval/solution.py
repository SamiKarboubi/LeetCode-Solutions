class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []
        inserted = False

        for start, end in intervals:
            if end < newInterval[0]:
                new_intervals.append([start, end])
            elif start > newInterval[1]:
                if not inserted:
                    new_intervals.append(newInterval)
                    inserted = True
                new_intervals.append([start, end])
            else:
                newInterval = [min(newInterval[0], start),max(newInterval[1], end)]
        if not inserted:
            new_intervals.append(newInterval)

        return new_intervals
