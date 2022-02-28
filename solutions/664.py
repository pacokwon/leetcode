# Maximum Width of a Binary Tree

from typing import Optional
from queue import Queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = Queue()

        cache = {}
        ans = 1

        # tree is guaranteed to have at one node.
        # (level, width, tree)
        q.put((0, 0, root))

        while not q.empty():
            level, width, tree = q.get()
            if level not in cache:
                cache[level] = [width, None]
            else:
                cl = cache[level]

                if width < cl[0]:
                    cl[0] = width

                if cl[1] is None or cl[1] < width:
                    cl[1] = width

                ans = max(ans, cl[1] - cl[0] + 1)

            if tree.left is not None:
                q.put((level + 1, 2 * width, tree.left))

            if tree.right is not None:
                q.put((level + 1, 2 * width + 1, tree.right))

        return ans

# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))
#     root = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)))
#     root = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
#     print(sol.widthOfBinaryTree(root))
