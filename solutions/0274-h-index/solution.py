class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h_index = 0
        for i in range(len(citations)):
            if citations[i] >= len(citations) - i and len(citations) - i >= h_index:
                h_index = len(citations) - i
        return h_index
