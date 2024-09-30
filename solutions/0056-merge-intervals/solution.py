class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals :
            return []
        intervals.sort(key=lambda x: x[0])
        merge=[intervals[0]]
        for i in range(1,len(intervals)):
            if merge[-1][1]>=intervals[i][0]:
                merge[-1][1]=max(intervals[i][1],merge[-1][1])
            else:
                merge.append(intervals[i])
        return merge
            

