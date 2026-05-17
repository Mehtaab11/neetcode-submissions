# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, maxValue):
            if not root:
                return 0

            count = 0

            if maxValue <= root.val:
                count = 1

            maxValue = max(maxValue, root.val)
            right = dfs(root.right, maxValue)
            left = dfs(root.left, maxValue)

            return count + left + right

        return dfs(root, root.val)
