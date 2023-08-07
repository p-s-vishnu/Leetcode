# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        With global variable
        T:O(n)
        S:O(logn)
        """
        if not root.left and not root.right:
            return root.val
        
        max_sum = [root.val]
        def dfs(node):
            if node is None:
                return 0
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)
            
            max_sum[0] = max(max_sum[0], node.val+left_max+right_max)
            return node.val + max(left_max, right_max)
            
        dfs(root)
        return max_sum[0]
        
        
""" Without global variable
         def dfs(root):
             if not root:
                 return 0, float("-inf") 
             left, wl = dfs(root.left)
             left = max(left,0)
            
             right, wr = dfs(root.right)
             right = max(right,0)
            
             res = max(wl, wr, root.val+left+right)
             return root.val+max(left,right) , res
       
         return dfs(root)[1]
"""