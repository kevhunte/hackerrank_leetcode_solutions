# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        copy = head
        
        if not head:
            return False
        
        fast = head.next
        
        while fast:
            
            if head == fast:
                return True
            head = head.next
            
            if fast.next:
                fast = fast.next.next
                continue
                
            return False
            
        
        return False