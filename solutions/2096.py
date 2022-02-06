# Step-By-Step Directions From a Binary Tree Node to Another
# Took so long T-T

from typing import Optional, List, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getPathTo(self, root: Optional[TreeNode], value: int, path: List[Tuple[int, str]]) -> bool:
        if root is None:
            return False

        if root.val == value:
            # finished
            path.append((root.val, 'F'))
            return True

        # go left
        path.append((root.val, 'L'))
        exists = self.getPathTo(root.left, value, path)
        if exists:
            return True
        path.pop()

        # go right
        path.append((root.val, 'R'))
        exists = self.getPathTo(root.right, value, path)
        if exists:
            return True
        path.pop()

        return False


    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        startPath = []
        self.getPathTo(root, startValue, startPath)

        destPath = []
        self.getPathTo(root, destValue, destPath)

        # start comparing paths
        length = min(len(startPath), len(destPath))
        index = 0
        while index < length:
            if startPath[index][0] != destPath[index][0]:
                break
            index += 1

        # either start is dest's ancester, or the other way around
        if index == length:
            if length == len(startPath):
                path = [x[1] for x in destPath[length-1:-1]]
            else:
                path = ['U'] * (len(startPath) - len(destPath))
        else:
            path = ['U'] * (len(startPath) - index)
            for i in range(index - 1, len(destPath) - 1):
                path.append(destPath[i][1])

        return ''.join(path)

# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(5,TreeNode(1,TreeNode(3),TreeNode(0,TreeNode(7))),TreeNode(2,TreeNode(6),TreeNode(4)))
#     startValue = 3
#     destValue = 7
#     root = TreeNode(2,TreeNode(1))
#     startValue = 2
#     destValue = 1
#     root = TreeNode(3,TreeNode(2,TreeNode(1,None,TreeNode(0))))
#     startValue = 2
#     destValue = 0
#     print(sol.getDirections(root, startValue, destValue))
