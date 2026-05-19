# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxHeight(root):
            if not root:
                return 0
            return 1+max(maxHeight(root.left),maxHeight(root.right))
        if not root:
            return 0
        leftHeight = maxHeight(root.left)
        rightHeight = maxHeight(root.right)
        diameter = leftHeight+rightHeight
        return max(diameter,max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right)))


        