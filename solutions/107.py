# Binary Tree Level Order Traversal II

from typing import Optional, List
from queue import Queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        if root is None:
            return []

        q = Queue()
        q.put((root, 1))
        while not q.empty():
            tree, level = q.get()

            if level == len(ans) + 1:
                ans.append([tree.val])
            elif level <= len(ans):
                ans[level - 1].append(tree.val)
            else:
                raise ValueError("Error!")

            if tree.left is not None:
                q.put((tree.left, level + 1))

            if tree.right is not None:
                q.put((tree.right, level + 1))

        return list(reversed(ans))

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    root = None
    print(sol.levelOrderBottom(root))
