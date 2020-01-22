# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#the recursive solution is first, and the iterative way is commented out below it
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        copy = head
        if(not head):   #if empty just return that
            return copy
        else:
            if(not head.next):  #if odd just return what you have
                return copy
            temp = head.val     #swap vals
            head.val = head.next.val
            head.next.val = temp
            self.swapPairs(head.next.next)
        '''while(head):
            if(not head.next):  #if odd just return what you have
                return copy
            temp = head.val     #swap vals
            head.val = head.next.val
            head.next.val = temp
            
            head = head.next.next'''
            
        return copy
