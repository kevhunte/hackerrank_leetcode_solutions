# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        copy = head
        last = head
        
        if head is None:
            return head
        
        head = head.next
        
        while head is not None:
            if last.val == head.val:
                last.next = head.next
            else:
                last = head
            head = head.next
        
        return copy