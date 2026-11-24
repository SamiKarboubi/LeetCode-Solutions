# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:

        def count_from(node, remaining):
            if not node:
                return 0
            remaining -= node.val
            return count_from(node.right,remaining) + count_from(node.left,remaining) + (remaining == 0)

        if not root:
            return 0
        
        return (count_from(root, targetSum)
                + self.pathSum(root.left, targetSum)
                + self.pathSum(root.right, targetSum))

        
