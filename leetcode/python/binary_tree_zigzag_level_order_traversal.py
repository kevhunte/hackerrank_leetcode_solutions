# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # same as last time, but switch order on each loop. flip == 0 level, else level = reversed(level)
        
        level = [root] if root else []
        
        ans = []
        reverse = False
        
        while level:
            layer = []
            queue = []
            
            for node in level:
                layer.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level = queue
            if reverse:
                layer.reverse()
            ans.append(layer)
            reverse = not reverse
            
        
        return ans