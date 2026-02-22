# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque([root])
        compteur = 0

        if not root:
            return []
        while queue:
            level_result = []
            level_size = len(queue)

            for _ in range(level_size):

                node = queue.popleft()
                level_result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if compteur % 2 == 1:
                level_result.reverse()
            compteur += 1
            result.append(level_result)


        return result
