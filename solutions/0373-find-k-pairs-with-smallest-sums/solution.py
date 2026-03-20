import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []

        heap = []
        result = []

        # On ne prend que les k premiers éléments de nums1 au départ
        for i in range(min(k, len(nums1))):
            # On commence toujours avec nums2[0]
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        while heap and len(result) < k:
            s, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            # On avance dans la ligne i
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return result

        

        
            




