# Definition for a binary tree node.

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getInorder(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        left = self.getInorder(root.left)
        right = self.getInorder(root.right)

        left.append(root.val)
        left.extend(right)
        return left

    def mergeTwo(self, l: List[int], r: List[int]) -> List[int]:
        left = 0
        right = 0

        ans = [0] * (len(l) + len(r))
        length = 0

        while left < len(l) and right < len(r):
            if l[left] < r[right]:
                ans[length] = l[left]
                length += 1
                left += 1
            else:
                ans[length] = r[right]
                length += 1
                right += 1

        while left < len(l):
            ans[length] = l[left]
            length += 1
            left += 1

        while right < len(r):
            ans[length] = r[right]
            length += 1
            right += 1

        return ans

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        arr1 = self.getInorder(root1)
        arr2 = self.getInorder(root2)
        return self.mergeTwo(arr1, arr2)

if __name__ == "__main__":
    sol = Solution()
    root1 = TreeNode(2, TreeNode(1), TreeNode(4))
    root2 = TreeNode(1, TreeNode(0), TreeNode(3))
    root1 = TreeNode(1, None, TreeNode(8))
    root2 = TreeNode(8, TreeNode(1))

    root1 = None
    root2 = TreeNode(5,TreeNode(1))
    print(sol.getAllElements(root1, root2))
