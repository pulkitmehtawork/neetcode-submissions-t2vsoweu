# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, r: Optional[TreeNode], s: Optional[TreeNode]) -> bool:

        
        if not s:
            return True
        
        if not r:
            return False

        if self.sametree(r, s):
            return True
        
        return (self.isSubtree(r.left, s)) or (self.isSubtree(r.right, s))
        





    def sametree(self , r, s):
        if not s and not r:
            return True

        if r and s and r.val == s.val:
            return self.sametree(r.left, s.left) and self.sametree(r.right, s.right)
        return False
        