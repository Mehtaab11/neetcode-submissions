# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def getD(root):
            if not root:
                return 0

            left = getD(root.left) 
            right = getD(root.right) 

            self.diameter = max(self.diameter, left + right)
            # 3 + 1 , it becomes 4 which is right answer

            return 1 + max(left, right)

        getD(root)
        return self.diameter
