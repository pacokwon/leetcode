# Container With Most Water

class Solution:
    def calcArea(self, heights, left, right):
        return (right - left) * min(heights[left], heights[right])

    def maxArea(self, heights):
        length = len(heights)
        area = 0
        left, right = 0, length - 1
        while left < right:
            area = max(area, self.calcArea(heights, left, right))

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return area

if __name__ == "__main__":
    sol = Solution()
    inp = [2,3,4,5,18,17,6]
    print(sol.maxArea(inp))
