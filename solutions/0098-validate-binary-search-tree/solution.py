# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        self.prev = None
        self.result = True
        def helper(root):
            if not root:
                return 
            helper(root.left)
            if self.prev:
                if self.prev.val >= root.val:
                    self.result = False
            self.prev = root
            helper(root.right)
        helper(root)
        return self.result
