# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            lenQ = len(q)

            for i in range(lenQ):
                rightNode = q.popleft()

                # This chaining of conditions is really important
                if rightNode:
                    # Only append if left node has any value
                    if rightNode.left:
                        q.append(rightNode.left)
                    # Only append if right node has any value
                    if rightNode.right:
                        q.append(rightNode.right)

            if rightNode:
                res.append(rightNode.val)

        return res
