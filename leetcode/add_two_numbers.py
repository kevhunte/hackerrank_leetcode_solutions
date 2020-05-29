# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        remainder = 0
        digit = 0
        front = ans = ListNode()
        while(l1 is not None and l2 is not None):
            newSum = l1.val + l2.val + ans.val
            digit = newSum % 10
            remainder = int((newSum - digit) / 10)
            ans.val = digit
            #print(1,ans.val, remainder)
            
            l1 = l1.next
            l2 = l2.next
            if(l1 is not None or l2 is not None or remainder > 0):
                ans.next = ListNode(val=remainder)
            ans = ans.next
            
        while(l1 is not None):
            newSum = l1.val + ans.val
            digit = newSum % 10
            remainder = int((newSum - digit) / 10)
            ans.val = digit
            #print(2,ans.val, remainder)
            
            l1 = l1.next
            if(l1 is not None or remainder > 0):
                ans.next = ListNode(val=remainder)
            ans = ans.next
            
        while(l2 is not None):
            newSum = l2.val + ans.val
            digit = newSum % 10
            remainder = int((newSum - digit) / 10)
            ans.val = digit
            #print(3,ans.val, remainder)
            
            l2 = l2.next
            if(l2 is not None or remainder > 0):
                ans.next = ListNode(val=remainder)
            ans = ans.next
            
        return front
            
        
