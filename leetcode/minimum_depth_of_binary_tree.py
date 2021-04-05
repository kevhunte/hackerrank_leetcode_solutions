# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
#       DFS
#     def helper(root,count, min_count):
#         if not root.left and not root.right:
#             return min(count,min_count)
        
#         if count > min_count:
#             return min_count
        
#         left = right = min_count
        
#         if root.left:
#             left = Solution.helper(root.left,count+1,min_count)
#         if root.right:
#             right = Solution.helper(root.right,count+1,min_count)
#         return min(left,right)
    
#     def minDepth(self, root: TreeNode) -> int:
#         # DFS, if more than one level, return ans
#         ans = Solution.helper(root,1,sys.maxsize) if root else 0
        
#         return ans
    
    # BFS
    def minDepth(self, root: TreeNode) -> int:
        
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
                if not node.left and not node.right:
                    return count
            level = queue
        
        return count