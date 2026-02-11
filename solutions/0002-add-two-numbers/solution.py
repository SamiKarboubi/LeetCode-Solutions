# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        previous = dummy
        un = 0
        while l1 or l2 or un:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            s = val1 + val2 + un
            if l2:
                l2 = l2.next
            if l1:
                l1 = l1.next
            current = ListNode(s % 10)
            previous.next = current
            un = s // 10
            previous = current
        
        return dummy.next
