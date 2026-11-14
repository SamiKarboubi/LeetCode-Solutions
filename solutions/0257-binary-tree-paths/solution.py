# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        stack = [(root, str(root.val))]
        result = []
        while stack:
            node, road = stack.pop()
            if node.right:
                stack.append((node.right, road + "->" + str(node.right.val)))
            if node.left:
                stack.append((node.left, road + "->" + str(node.left.val)))
            if not node.right and not node.left:
                result.append(road)
        return result
