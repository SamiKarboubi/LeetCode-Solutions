# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        current = head
        l = 1

        while current.next:
            current = current.next
            l += 1
        current.next = head
        current = head
        k = k%l
        for _ in range(l-k-1):
            current = current.next
        n = current.next
        current.next = None

        return n
