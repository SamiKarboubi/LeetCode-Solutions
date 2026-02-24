# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.answer = None
        self.index = 1

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if self.index == k:
                self.answer = root.val
            self.index += 1
            inorder(root.right)

        inorder(root)

        return self.answer


 

        
