# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if(not l1 and not l2):
            return None
        ptr = copy = ListNode()
        # go through list. Put the bigger one in the new list and move along ptr
        while(l1 and l2):
            if(l1.val > l2.val):    #add smallest, move to next
                ptr.val = l2.val
                l2 = l2.next
            else:
                ptr.val = l1.val
                l1 = l1.next
            if(l1 or l2):           #check if next val
                ptr.next = ListNode()
                ptr = ptr.next

        while(l1):
            ptr.val = l1.val
            l1 = l1.next
            if(l1):
                ptr.next = ListNode()
                ptr = ptr.next
        while(l2):
            ptr.val = l2.val
            l2 = l2.next
            if(l2):
                ptr.next = ListNode()
                ptr = ptr.next
        return copy
