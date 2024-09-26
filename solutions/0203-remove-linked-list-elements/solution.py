# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val:
            head=head.next
        if not head:
            return head
        current=head
        while current and current.next:
            if current.next.val==val:
                current.next=current.next.next
            else:
                current=current.next
        return head
        
