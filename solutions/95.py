# Unique Binary Trees II

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def helper(start: int, n: int) -> List[Optional[TreeNode]]:
            if n == 0:
                return [None]

            result = []
            for i in range(n):
                # i nodes on the left,
                # n - i - 1 nodes on the right

                left = helper(start, i)
                right = helper(start + i + 1, n - i - 1)

                for l in left:
                    for r in right:
                        result.append(TreeNode(0, l, r))

            return result

        def fill(start: int, tree: Optional[TreeNode]) -> int:
            if tree is None:
                return start

            ln = fill(start, tree.left)
            tree.val = ln
            rn = fill(ln + 1, tree.right)
            return rn

        result = helper(1, n)
        for t in result:
            fill(1, t)

        return result

if __name__ == "__main__":
    sol = Solution()
    n = 3
    sols = sol.generateTrees(n)
    print(sols[2].val, sols[2].left.val, sols[2].right.val)
    print(sols, len(sols))
