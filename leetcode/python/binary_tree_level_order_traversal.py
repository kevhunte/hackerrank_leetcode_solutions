# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # create and return the queue of the BFS
        # when going through the children, add the val to the list to return
        level = [root] if root else []
        
        ans = []
        
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
            ans.append(layer)
            
        return ans
        