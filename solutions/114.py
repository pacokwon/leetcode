
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        ltip = self.helper(root.left)
        rtip = self.helper(root.right)

        if ltip is None and rtip is None:
            return root

        if ltip is None:
            # rtip is not None
            return rtip

        if rtip is None:
            root.right = root.left
            root.left = None
            return ltip

        ltip.right = root.right
        root.right = root.left
        root.left = None

        return rtip

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.helper(root)

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(5,None,TreeNode(6)))
    sol.flatten(root)
    print(root.left.val)
