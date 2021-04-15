# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(root, arr):
        if not root.left and not root.right:
            return root.val
        
        arr.append(root.val)
        
        if root.left:
            val = Solution.helper(root.left, arr)
            if val:
                arr.append(val)
        if root.right:
            val = Solution.helper(root.right, arr)
            if val:
                arr.append(val)
    
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        arr = []
        Solution.helper(root, arr)
        return arr if arr else [root.val]