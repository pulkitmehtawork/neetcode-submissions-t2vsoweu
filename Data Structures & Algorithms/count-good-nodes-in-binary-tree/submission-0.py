# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:



        def dfs(maxVal, node):
            if not node:
                return 0


            if node.val >= maxVal:
                res = 1
            else:
                res = 0

            maxVal = max(maxVal , node.val)
            res += dfs(maxVal , node.left)
            res += dfs(maxVal , node.right)
            return res

        return dfs(root.val , root)

        