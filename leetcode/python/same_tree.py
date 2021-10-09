# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSame(p,q):
        pn = p is None
        qn = q is None
        
        # base case
        if pn and qn:
            return True
        elif pn ^ qn:
            return False
        
        if p.val == q.val:
            l_result = Solution.isSame(p.left, q.left)
            r_result = Solution.isSame(p.right, q.right)
            if l_result and r_result:
                return True
            else:
                return False
        else:
            return False
    
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        result = Solution.isSame(p,q)
        
        return result