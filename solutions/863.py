from typing import Optional, List
from queue import Queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def fillParent(self, root: Optional[TreeNode]):
        if root is None:
            return

        root.visited = False

        if root.left is not None:
            root.left.parent = root
            self.fillParent(root.left)

        if root.right is not None:
            root.right.parent = root
            self.fillParent(root.right)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.fillParent(root)
        root.parent = None

        q = Queue()
        # node, dist from target
        q.put((target, 0))
        target.visited = True
        ans = []

        while not q.empty():
            node, dist = q.get()
            if dist == k:
                ans.append(node.val)
                continue

            if node.left is not None and not node.left.visited:
                node.left.visited = True
                q.put((node.left, dist + 1))

            if node.right is not None and not node.right.visited:
                node.right.visited = True
                q.put((node.right, dist + 1))

            if node.parent is not None and not node.parent.visited:
                node.parent.visited = True
                q.put((node.parent, dist + 1))

        return ans
