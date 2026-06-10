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

            # diameter will become left + right
            # why ?
            # if left
            # beacuase left has 2 depth and right has 2 depth
            # Then the dia will become 4

            # so for any given parent node diameter is both left + right

            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)

        getD(root)
        return self.diameter
