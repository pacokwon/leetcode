# Jump Game

class Solution:
    def canJump(self, nums):
        pos = 0
        target = len(nums) - 1
        visited = [False] * len(nums)

        while pos < target:
            if visited[pos]:
                return False

            visited[pos] = True
            dist = nums[pos]
            if dist == 0:
                pos -= 1

            oldPos = pos
            pos += dist

        return True
