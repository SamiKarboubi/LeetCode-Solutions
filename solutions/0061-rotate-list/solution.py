# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k==0 or not head or not head.next:
            return head
        current=head
        len=1
        while current.next:
            current=current.next
            len+=1
        current.next=head
        k=k%len
        if k==0:
            current.next=None
            return head
        
        m=head
        for _ in range(len-k-1):
            m=m.next
        head=m.next
        m.next=None
        return head

 





