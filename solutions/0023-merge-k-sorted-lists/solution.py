# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        heap = [(node.val,i,node) for i, node in enumerate(lists) if node]
        heapq.heapify(heap)
        dummy = tail = ListNode()
        while heap:
            _, i, node = heap[0]
            tail.next = node
            tail = node
            if node.next:
                heapq.heapreplace(heap,(node.next.val,i,node.next))
            else:
                heapq.heappop(heap)
        return dummy.next
