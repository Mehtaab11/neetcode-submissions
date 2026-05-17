# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        self.res = []

        def inOrder(root):
            if not root:
                return

            inOrder(root.left)
            self.res.append(root.val)
            inOrder(root.right)

        inOrder(root)

        return all(self.res[i] < self.res[i + 1] for i in range(len(self.res) - 1))
