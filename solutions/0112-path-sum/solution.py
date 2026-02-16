# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False

        if not root.left and not root.right:
            if root.val == targetSum:
                return True
            else:
                return False

        
        

        newTargetSum = targetSum - root.val
        return self.hasPathSum(root.left, newTargetSum) or self.hasPathSum(root.right, newTargetSum)
