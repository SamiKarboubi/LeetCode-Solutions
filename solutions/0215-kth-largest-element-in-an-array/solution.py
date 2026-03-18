class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []

        def perm(i, j):
            heap[i], heap[j] = heap[j], heap[i]

        def add_to_heap(val):
            heap.append(val)
            i = len(heap) - 1
            parent = (i - 1) // 2
            while i > 0 and heap[parent] > heap[i]:
                perm(i, parent)
                i = parent
                parent = (i - 1) // 2

        def drop_element(i, heap_size):
            while True:
                left = 2*i + 1
                right = 2*i + 2
                smallest = i

                if left < heap_size and heap[left] < heap[smallest]:
                    smallest = left
                if right < heap_size and heap[right] < heap[smallest]:
                    smallest = right

                if smallest == i:
                    break
                perm(i, smallest)
                i = smallest

        
        for num in nums:
            if len(heap) < k:
                add_to_heap(num)          
            elif num > heap[0]:
                heap[0] = num             
                drop_element(0, k)        

        return heap[0] 
