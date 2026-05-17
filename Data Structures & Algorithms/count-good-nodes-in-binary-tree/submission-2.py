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

            if root.val >= maxValue:
                count += 1
                maxValue = root.val
            left = dfs(root.left, maxValue)
            right = dfs(root.right, maxValue)

            return count + left + right

        return dfs(root, root.val)
