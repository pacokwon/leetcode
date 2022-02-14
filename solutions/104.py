# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        ld = self.maxDepth(root.left)
        rd = self.maxDepth(root.right)

        return max(ld, rd) + 1

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    root = TreeNode(3, TreeNode(9))
    print(sol.maxDepth(root))
