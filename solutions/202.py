# Happy Number

class Solution:
    def getNext(self, n):
        added = 0
        while n != 0:
            added += (n % 10) ** 2
            n = n // 10

        return added

    def isHappy(self, n):
        visited = set()

        while n != 1:
            if n in visited:
                return False

            visited.add(n)
            n = self.getNext(n)

        return True

if __name__ == "__main__":
    sol = Solution()
    n = 2
    print(sol.isHappy(n))
