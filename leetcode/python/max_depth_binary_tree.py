# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # DFS / Recursive
    def maxDepth(self, root: TreeNode) -> int:
        # recurse in a helper, return the num of calls at the leaf
        # take the max of all runs
        def depthHelper(node,count):
            if node is None:
                return count
            
            left = depthHelper(node.left,count+1)
            right = depthHelper(node.right,count+1)
            
            return max(left,right)
        
        
        #ans = depthHelper(root,0)
        
        return depthHelper(root,0) #ans

    # BFS / Iterative 
    def maxDepth(self, root: TreeNode) -> int:
        # BFS, inc for each level
        
        level = [root] if root else []
        
        count = 0
        
        while level:
            count += 1
            queue = []
            
            for node in level:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            level = queue
        
        return count