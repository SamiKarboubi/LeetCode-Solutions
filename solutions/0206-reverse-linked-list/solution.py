# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        current = head
        prev = None
        while current:
            stock = current.next
            current.next = prev
            prev = current
            current = stock       
        return prev
