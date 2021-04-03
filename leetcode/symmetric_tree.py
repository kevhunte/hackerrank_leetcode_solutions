# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # traverse the tree, but swap the paths in each recursive call
        def treeCompare(left,right):
            lNone = left is None
            rNone = right is None
            if lNone and rNone:
                return True
            elif lNone ^ rNone:
                return False
            #print('treeCompare:',left.val,right.val)
            if left.val == right.val:
                lAns = treeCompare(left.left,right.right)
                rAns = treeCompare(left.right,right.left)
                
                if lAns and rAns:
                    return True
                else:
                    return False
            else:
                return False
        #print('Test Case', end='\n\n')
        if root is None:
            return True
        else:
            return treeCompare(root.left,root.right)
        