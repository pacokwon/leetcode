# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def aux(self, root: TreeNode, max_val: int) -> int:
        if root is None:
            return 0

        new_max = max(max_val, root.val)

        left = self.aux(root.left, new_max)
        right = self.aux(root.right, new_max)
        return left + right + (0 if max_val > root.val  else 1)

    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return self.aux(root, root.val)

