# First Bad Version

# The isBadVersion API is already defined for you.
def isBadVersion(version):
    return version >= 4

class Solution:
    def firstBadVersion(self, n):
        left = 1
        right = n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid     # scope is narrowed to [left, mid]
            else:
                left = mid + 1  # scope is narrowed to (mid, right]

        return left

if __name__ == "__main__":
    sol = Solution()
    print(sol.firstBadVersion(5))
