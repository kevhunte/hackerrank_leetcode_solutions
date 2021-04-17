# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, path) -> int:
        if root:
            path.append(root.val)
            if not root.left and not root.right:
                val = 0
                for p in path:
                    val *= 10
                    val += p
                return val
            left = right = 0
            if root.left:
                left = self.helper(root.left, path)
                path.pop()
            if root.right:
                right = self.helper(root.right, path)
                path.pop()
            return left+right
        else:
            return 0
    
    def sumNumbers(self, root: TreeNode) -> int:
        # make list of path. At leaf, convert to number and return
        return self.helper(root,[])
        