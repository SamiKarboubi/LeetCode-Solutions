# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        index = {}
        for i in range(len(inorder)):
            index[inorder[i]] = i

        self.i = 0

        def helper(in_left,in_right):

            if in_left > in_right:
                return None
            root = TreeNode(preorder[self.i])
            self.i += 1
            index_in_order = index[root.val]
            root.left = helper(in_left,index_in_order-1)
            root.right = helper(index_in_order+1,in_right)

            return root

        return helper(0,len(preorder)-1)





        




        
