# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def inorderRoot(root):
            if not root:
                return 
            inorderRoot(root.left)
            res.append(root.val)
            inorderRoot(root.right)
        inorderRoot(root)
        print(res)
        return res[k-1]