# Balanced Binary Tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def helper(t):
            if t is None:
                return (0, True)

            lh, lb = helper(t.left)
            rh, rb = helper(t.right)
            if not (lb and rb):
                # height doesn't matter anymore.
                return (0, False)

            return (1 + max(lh, rh), abs(lh - rh) <= 1)

        return helper(root)[1]

if __name__ == "__main__":
    sol = Solution()
    node = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
    node = TreeNode(3,TreeNode(9))
    node = TreeNode(3,TreeNode(2,TreeNode(3,TreeNode(4),TreeNode(4)),TreeNode(3)),TreeNode(20))
    node = TreeNode(1,TreeNode(2,TreeNode(3,TreeNode(4))),TreeNode(2,None,TreeNode(3,None,TreeNode(4))))
    print(sol.isBalanced(node))
