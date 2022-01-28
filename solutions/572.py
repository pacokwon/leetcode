# Subtree of Another Tree

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEqual(self, root, sub):
        if root is not None and sub is not None:
            return (
                root.val == sub.val and
                self.isEqual(root.left, sub.left) and
                self.isEqual(root.right, sub.right)
            )

        return root is None and sub is None


    def isSubtree(self, root, subRoot):
        if self.isEqual(root, subRoot):
            return True

        if root is None and subRoot is not None:
            return False

        # not equal
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
    subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
    print(sol.isSubtree(subRoot, None))
