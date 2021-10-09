# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # while l1 and l2 are not None. Make space for current val
        # If only one list, make room as there is a val
        # check l1.val against l2.val. append biggest to l3
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        # at this point, both lists contain data
        
        head = l3 = ListNode()
        
        while l1 is not None and l2 is not None:
            l3.next = ListNode() # there's always a next val, because we are comparing
            if l2.val <= l1.val:
                l3.val = l2.val
                l2 = l2.next
            else:
                l3.val = l1.val
                l1 = l1.next
            l3 = l3.next
            
        #print('l1:', l1, '\nl2:', l2)
        
        # if next exists, allocate space for it
        while l1 is not None:
            l3.val = l1.val
            l1 = l1.next
            if l1 is not None:
                l3.next = ListNode()
                l3 = l3.next
        while l2 is not None:
            l3.val = l2.val
            l2 = l2.next
            if l2 is not None:
                l3.next = ListNode()
                l3 = l3.next
        
        return head