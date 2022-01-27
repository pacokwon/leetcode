# Merge Two Binary Trees

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1, root2):
        if root1 is None:
            return root2

        if root2 is None:
            return root1

        newLeft = self.mergeTrees(root1.left, root2.left)
        newRight = self.mergeTrees(root1.right, root2.right)
        newTreeNode = TreeNode(root1.val + root2.val, newLeft, newRight)

        return newTreeNode

if __name__ == "__main__":
    sol = Solution()
    root1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
    root2 = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))

    root1 = None
    root2 = None
    print(sol.mergeTrees(root1, root2))
