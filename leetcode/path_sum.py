# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(root, target, count):
        if not root.left and not root.right:
            return count + root.val == target
        
        leftval = rightval = None
        
        if root.left:
            leftval = Solution.helper(root.left, target, count+root.val)
        if root.right:
            rightval = Solution.helper(root.right, target, count+root.val)
        
        return leftval or rightval
    
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # DFS with helper. Count sum of path. If output equals target sum, return true
        ans = Solution.helper(root, targetSum, 0) if root else False
        
        return ans