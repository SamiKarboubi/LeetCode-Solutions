# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def helper(root,prev):

            if not root:
                return prev
            
            prev = helper(root.right,prev)


            prev = helper(root.left,prev)

            root.right = prev
            root.left = None
            prev = root

            return prev


        helper(root,None)






