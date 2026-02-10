# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head.next:
            return None
        current_fast = head
        compteur = 0
        dummy = ListNode(0)
        dummy.next = head
        current_slow = dummy

        while current_fast:
            
            current_fast = current_fast.next

            if compteur == n:
                current_slow = current_slow.next
            else:
                compteur += 1

        current_slow.next = current_slow.next.next

        return dummy.next


