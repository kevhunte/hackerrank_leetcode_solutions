# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def getLength(head: ListNode):
            l = 1
            while(head.next):
                l+=1
                head = head.next
            return l
        #### helper func ^ ####
        start = head    #copy of pointer
        if(n < 1):
            return []
        length = getLength(head)    #gets length of list
        head = start
        index2remove = length - n + 1
        if(index2remove == 1):      #remove first element
            return head.next
        else:
            while(index2remove > 1):
                if(index2remove == 2):  #somewhere in middle
                    head.next = head.next.next
                    break
                elif(index2remove == 1):    #last element
                    head.next = None
                    break
                head = head.next
                index2remove-=1
            return start
