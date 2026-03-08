# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def split(self,head):
        if not head:
            return
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        return head,slow

    def merge(self,fpart,spart):
        dummy = ListNode()
        current = dummy
        while fpart and spart:
            if fpart.val > spart.val:
                current.next = spart
                spart = spart.next
            else:
                current.next = fpart
                fpart = fpart.next
            current = current.next
        current.next = fpart or spart
        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        fpart,spart = self.split(head)
        fpart = self.sortList(fpart)
        spart = self.sortList(spart)

        return self.merge(fpart,spart)

