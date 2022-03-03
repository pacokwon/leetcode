from functools import lru_cache

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode) -> int:
        @lru_cache(None)
        def helper(node):
            if node is not None:
                return 0

            profit = node.val
            if node.left is not None:
                profit += helper(node.left.left) + helper(node.left.right)

            if node.right is not None:
                profit += helper(node.right.left) + helper(node.right.right)

            return max(profit, helper(node.left) + helper(node.right))

        return helper(root)

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3, TreeNode(2, None, TreeNode(3)), TreeNode(3, None, TreeNode(1)))
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(3)), TreeNode(5, None, TreeNode(1)))
    print(sol.rob(root))
