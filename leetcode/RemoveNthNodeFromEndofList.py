# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #find length of list (edge, check when empty)
        #go through again and delete the node at that spot
        copy = head
        
        if head is None or head.next is None:
            #print('empty list:', head)
            return None
        
        length = 1
        
        #gets length of list
        while head.next is not None:
            length += 1
            head = head.next
        
        #print('length:',length) # test passed
        
        #reset pointer
        head = copy
        
        #index before one to delete
        initDelete = length - n - 1
        
        #print('start deleting at this position:',initDelete) # test
        
        #check 1
        # if n is 1, taking off end of list
        # make head.next = head.next.next
        for i in range(length):
            ##print('iteration val:',i) # logs
            if -1 is initDelete and n is 1 and length is 1:
                ##print('I was given an empty list.', 'list:',head) # test
                return None
            if i is initDelete and n is 1:
                ##print('I was given a list of 1','list:',head) # test
                head.next = None
                return copy
            if -1 is initDelete and n is length:
                #print('I was given greater than 1 and 1st to delete') # test
                return copy.next
            if i is initDelete:
                ##print('I was given a list to delete greater than 1 and in the middle','list:',head) # test passed
                head.next = head.next.next
                return copy
            head = head.next
            
        #print('You didn\'t think about me.', '\ninitDelete:',initDelete, '\npointer:', head)
        return copy